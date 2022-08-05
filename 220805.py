from xml.dom.minidom import Element
import numpy as np
import pandas as pd
import requests, json, os
from PIL import Image as pil
import scrapy



# ### G마켓 이미지
# # csv 파일 불러오기
# df = pd.read_csv('csv/gmarket.csv')
# print(df)

# # 디렉토리 생성
# folder = 'Gmarket_img'
# if not os.path.exists(folder):
#     os.makedirs(folder)
    

# # 이미지 다운로드
# # img_link = df.loc[0, 'img']

# # response = requests.get(img_link)
# # with open(f'{folder}/img01.png', 'wb') as file:
#     # file.write(response.content)

# # enumerate 하는 경우 컬럼을 불러옴
# for idx, data in df[3:5].iterrows():
#     filename = "0" * (3 - len(str(idx))) + str(idx) + ".png"
    
#     response = requests.get(data["img"])
    
#     with open(f'{folder}/{filename}', 'wb') as file:
#         file.write(response.content)

# pil.open(f"{folder}/003.png")


### selenium
#  : 브라우저의 자동화 목적으로 만들어진 다양한 브라우저와 언어를 지원하는 라이브러리

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# def selenium_not_quit(drivePath, url):
#     # chrome 실행
#     driver = webdriver.Chrome(drivePath)

#     # 페이지 이동
#     driver.get(url)

#     # 페이지 사이즈
#     driver.set_window_size(200,600)

#     # 페이지 스크롤 조절 : 자바스크립트 코드
#     driver.execute_script("window.scrollTo(200,300)") 

#     # alert
#     # driver.execute_script("alert('hellow selenium!'")

#     driver.execute_script("window.scrollTo(0,0)") 

#     # input 문자열 입력
#     driver.find_element(By.CSS_SELECTOR, '#q').send_keys('pythone')

#     # 검색 버튼 클릭
#     driver.find_element(By.CSS_SELECTOR, '#daumSearch > fieldset > div > div > button.ico_pctop.btn_search').click()
    
#     while True:
#         pass
    
# driver_path = 'C:/Users/User/Desktop/driver/chromedriver.exe'
# url = "https://daum.net"

# # selenium_not_quit(driver_path, url)


# def selenium_not_quit(drivePath, url):
#     # chrome 실행
#     driver = webdriver.Chrome(drivePath)
#     # 페이지 이동
#     driver.get(url)

#     # By.CSS_SELECTOR
#     sub_title = driver.find_element(By.CSS_SELECTOR, '#banner-secondary').text
    
#     driver.find_element(By.CSS_SELECTOR, "#languages [lang='ko']").click()
    
#     # #shoji > div.shoji__door > div > div.main.talks-main
#     # #browse-results > div.row.row-sm-4up.row-lg-6up.row-skinny > div:nth-child(1) > div > div > div
#     elemnts = driver.find_elements(By.CSS_SELECTOR, '#browse-results > .row > div)')
    
#     print(elemnts)
    
# driver_path = 'C:/Users/User/Desktop/driver/chromedriver.exe'
# url = "https://ted.com/talks"

# print(selenium_not_quit(driver_path, url))




# # 모델 만들기
# from sklearn.linear_model import LinearRegression

# df = pd.read_csv('csv/premierleague.csv')

# print(df)

# feture = df[['gf','ga']]
# target = df['points']

# model = LinearRegression().fit(feture, target)

# print(np.round(model.predict([[80,36]])))

# # 모델 저장
# import pickle

# with open('model.pkl', 'wb') as file:
#     pickle.dump(model, file)
    

# # 모델 불러오기
# with open('model.pkl', 'rb') as file:
#     load_model = pickle.load(file)
    
# print(np.round(load_model.predict([[80,36]])))



