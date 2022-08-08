# 크롤링
import numpy as np
import pandas as pd
import requests, json
import scrapy
from bs4 import BeautifulSoup
import datetime
import matplotlib.pyplot as plt

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


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
    dt = BeautifulSoup(response.text, 'html.parser')
    elements = dt.select('#bestPrdList > div:nth-child(2) > ul > li')
    
    items = []
    for e in elements:
        tmp = {
            'title':e.select_one('.pname > p').text
            , 'price':e.select_one('.sale_price').text.replace('원','').replace(',','')
            , 'img':e.select_one('img').attrs['src']
        }
        items.append(tmp)
        
    df = pd.DataFrame(items)
    print(df)
    
# elevenMarket()



def elevenMarket_selenium():
    url = 'https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain'
    drive_path = 'C:/Users/mskyu/Desktop/driver/chromedriver.exe'

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # options.add_argument('headless')

    drive = webdriver.Chrome(drive_path, options=options)
    # drive = webdriver.Chrome(drive_path)

    drive.get(url)

    drive.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    
    SCROLL_PAUSE_SEC = 2
    last_height = drive.execute_script("return document.body.scrollHeight")

    while True:
        drive.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 1초 대기
        time.sleep(SCROLL_PAUSE_SEC)

        # 스크롤 다운 후 스크롤 높이 다시 가져옴
        new_height = drive.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break

        last_height = new_height

    drive.execute_script("window.scrollTo(0, 0);")
    selector = "#bestPrdList > .viewtype catal_ty > ul > li"
    elements = drive.find_elements(By.CSS_SELECTOR, selector)
    print(len(elements))
    items = []

    for e in elements:
        tmp = {
            'title':e.find_element(By.CSS_SELECTOR, '.pname > p').text
            , 'price':e.find_element(By.CSS_SELECTOR, '.sale_price').text.replace('원','').replace(',','')
            , 'img':e.find_element(By.CSS_SELECTOR, 'img').get_attribute('src')
        }
        items.append(tmp)
        
    drive.quit()
    return pd.DataFrame(items)
    

df = elevenMarket_selenium()
