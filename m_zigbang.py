
import pandas as pd
import geohash2, json, requests

def zigbang(addr):
    """zigbang room search

    Args:
        addr (str): address

    Returns:
        DataFrame: columns - ["item_id", "sales_type", "deposit", "rent", "size_m2", "address1", "manage_cost"]
    """
    
    url1 = f'https://apis.zigbang.com/v2/search?leaseYn=N&q={addr}&serviceType=원룸'
    
    dt1 = requests.get(url1).json()['items'][0]
    lat, lng = dt1['lat'],dt1['lng']
    geohash = geohash2.encode(lat, lng, precision=5)
    
    url2 = f'https://apis.zigbang.com/v2/items?deposit_gteq=0&domain=zigbang&geohash={geohash}&needHasNoFiltered=true&rent_gteq=0&sales_type_in=전세|월세&service_type_eq=원룸'
    
    dt2 = requests.get(url2).json()["items"]
    idx = [item['item_id'] for item in dt2]
    
    url3 = 'https://apis.zigbang.com/v2/items/list'
    
    params = {
        'domain': 'zigbang',
        'item_ids':idx,
        'withCoalition': 'true'
    }
    dt3 = requests.post(url=url3, params=params).json()['items']
    columns = ["item_id", "sales_type", "deposit", "rent", "size_m2", "address1", "manage_cost"]
    df = pd.DataFrame(dt3)[columns]
    
    
    return df