### 데이터 모델링 : 따릉이
# Data : 서울 공유 자전거
# 문제 : 2시간 후 수요 예측

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
from linear import default_modeling

path = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/SeoulBikeData2.csv'
data = pd.read_csv(path)

# 2시간 후 count
data['y'] = data['Count'].shift(-2)
data = data[:-2]

# 날짜 데이터 제거
data = data.drop('DateTime', axis=1)

# 가변수화
data = pd.get_dummies(data=data, columns=['Seasons', 'Holiday', 'FuncDay'], drop_first=True)

print(data.columns)

model1 = default_modeling(data, 'y')
model1.linear_modeling_all()

print(model1.model.coef_)
print(model1.model.intercept_)
print(model1.x)