# 크롤링
import numpy as np
import pandas as pd
import requests, json
import scrapy
from bs4 import BeautifulSoup
import datetime
import matplotlib.pyplot as plt


def naver_finance(size, page, code = 'KOSPI'):
    url = f'https://m.stock.naver.com/api/index/{code}/price?pageSize={size}&page={page}'

    response = requests.get(url)
    df = pd.DataFrame(response.json())[['localTradedAt', 'openPrice', 'closePrice']]
    
    df['openPrice'] = df['openPrice'].apply(lambda data: float(data.replace(',','')))
    df['closePrice'] = df['closePrice'].apply(lambda data: float(data.replace(',','')))
    
    return df


# naver_finance('10', '1')



def naver_api_search():
    id, pw = 'Y7kkW5s3waqiGemisIDm', 'O0iVtJhKyp'
    url = 'https://openapi.naver.com/v1/datalab/search'

    params = {
        "startDate": "2018-01-01",
        "endDate": datetime.datetime.now().strftime('%Y-%m-%d'),
        "timeUnit": "month",
        "keywordGroups": [
        {
            "groupName": "JAVA",
            "keywords": [
            "java"
            ]
        },
        {
            "groupName": "C",
            "keywords": [
            'c', 'c++'
            ]
        },
        {
            "groupName": "PYTHONE",
            "keywords": [
            'python','py'
            ]
        },
        {
            "groupName": "JS",
            "keywords": [
            'javascript','js'
            ]
        },
        ],
    }

    headers = {
        'Content-Type': 'application/json',
        'X-Naver-Client-Id': id,
        'X-Naver-Client-Secret': pw
    }

    lab_Data = requests.post(url, data=json.dumps(params) ,headers=headers)

    df = pd.DataFrame(lab_Data.json()['results'][0]['data'])['period']


    for i in range(len(params['keywordGroups'])):
        title = params['keywordGroups'][i]['groupName']
        df_ = pd.DataFrame(lab_Data.json()['results'][i]['data'])['ratio']
        df = pd.concat([df,df_], axis=1)
    
        df.rename(columns={'ratio':title}
                , inplace=True)


    return df

# lng = naver_api_search()

# lng.plot(figsize=(20, 5))
# plt.legend(loc=0)
# plt.show()



def elevenMarket():
    url = 'https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain'

    response = requests.get(url)
    selector = '#bestPrdList > div:nth-child(2) > ul > li'