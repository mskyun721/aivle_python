import requests, json
import pandas as pd

# requests def
def stock_crawling(pagesize, page, code='KOSPI'):
    """stock page crawling

    Args:
        pagesize (int): page size
        page (int): page number
        code (str, optional): KOSPI / KOSDAQ. Defaults to 'KOSPI'.

    Returns:
        DataFrame : 'localTradedAt', 'closePrice'
    """
    
    
    url = f'https://m.stock.naver.com/api/index/{code}/price?pageSize={pagesize}&page={page}'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)[['localTradedAt', 'closePrice']]
    
    return df

def exchange_crawling(pagesize, page, code='FX_USDKRW'):
    """money exchange

    Args:
        pagesize (int): page size
        page (int): page number
        code (str, optional): FX_USDKRW, FX_EURKRW, FX_JPYKRW, FX_CNYKRW, each. Defaults to 'FX_USDKRW'.

    Returns:
        _DataFrame : 'localTradedAt', 'closePrice'
    """
    
    url = f'https://api.stock.naver.com/marketindex/exchange/{code}/prices?page={page}&pageSize={pagesize}'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)[['localTradedAt', 'closePrice']]
    
    return df


# 피어스 상관계수 : df.corr()
kospi = stock_crawling(60, 1)
kosdaq = stock_crawling(60, 1, 'KOSDAQ')
usd = exchange_crawling(60,1)

df = kospi.copy()
df['kosdaq'] = kosdaq["closePrice"]
df['usd'] = usd["closePrice"]
df.rename(columns={'closePrice': 'kospi'},
          inplace=True)

# df type 변경
df['kospi'] = df['kospi'].apply(lambda data:float(data.replace(',','')))
df['kosdaq'] = df['kosdaq'].apply(lambda data:float(data.replace(',','')))
df['usd'] = df['usd'].apply(lambda data:float(data.replace(',','')))

print(df[['kospi', 'kosdaq', 'usd']].corr())


### naver api : papago
CLIENT_ID, CLIENT_SECRET = "Y7kkW5s3waqiGemisIDm", "O0iVtJhKyp"

def ppg_translate(id,pw,txt,fromNa='ko', toNa='en'):
    """naver papago translate api

    Args:
        id (str): naver api id
        pw (str): naver api secret_
        txt (str): befor translate text
        fromNa (str, optional): . Defaults to 'ko'.
        toNa (str, optional): . Defaults to 'en'.

    Returns:
        _type_: DataFrame, after translate text
    """
    
    params = {
        'source': fromNa,
        'target': toNa,
        'text':txt
    }
    
    headers = {
        "Content-Type": "application/json",
        "X-Naver-Client-Id": id,
        "X-Naver-Client-Secret": pw
    }
    response = requests.post('https://openapi.naver.com/v1/papago/n2mt', json.dumps(params), headers=headers)
    
    return response.json()["message"]["result"]["translatedText"]

print(ppg_translate(CLIENT_ID, CLIENT_SECRET, '크롤링 공부'))


### covid 번역
def ppg_translate_txt(txt):
    """naver papago translate api

    Args:
        txt (str): befor translate text

    Returns:
        _type_: DataFrame, after translate text
    """
    
    params = {
        'source': 'ko',
        'target': 'en',
        'text':txt
    }
    headers = {
        "Content-Type": "application/json",
        "X-Naver-Client-Id": CLIENT_ID,
        "X-Naver-Client-Secret": CLIENT_SECRET
    }
    
    response = requests.post('https://openapi.naver.com/v1/papago/n2mt', json.dumps(params), headers=headers)
    
    return response.json()["message"]["result"]["translatedText"]

covid = pd.read_excel("excel/covid.xlsx")[["category", "title"]]
covid['en'] = covid['title'].apply(ppg_translate_txt)
print(covid)
covid.to_excel('excel/covid_en.xlsx', index=False, encoding='utf-8-sig')



### 실습 과제
# https://finance.daum.net/exchanges
# headers : referer, user-agent 설정

url = 'https://finance.daum.net/api/exchanges/summaries'
headers = {
    'referer':'https://finance.daum.net/exchanges',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

daum_exchange = requests.get(url=url, headers=headers)
# daum_exchange = requests.get(url)
print(daum_exchange)
print(daum_exchange.text)
data = daum_exchange.json()['data']
df = pd.DataFrame(data)[['date', 'basePrice']]
print(df)


import m_zigbang

print(m_zigbang.zigbang('주례동'))