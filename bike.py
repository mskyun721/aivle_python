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

from linear import Linear
from knn import Knn
from logistic import Logistic

path = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/SeoulBikeData2.csv'
data = pd.read_csv(path)

# 2시간 후 count
data['y'] = data['Count'].shift(-2)
data = data[:-2]

# 날짜 데이터 제거
data = data.drop('DateTime', axis=1)

# 가변수화
data = pd.get_dummies(data=data, columns=['Seasons', 'Holiday', 'FuncDay'], drop_first=True)


# ------------------------------------------------------------------------------------------
path2 = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/mobile_cust_churn.csv'
data2 = pd.read_csv(path2)

drop_cols = ['id']
data2.drop(drop_cols, axis = 1, inplace = True )

dumm_cols = ['REPORTED_SATISFACTION','REPORTED_USAGE_LEVEL','CONSIDERING_CHANGE_OF_PLAN']
data2 = pd.get_dummies(data2, columns = dumm_cols, drop_first = True)
data2['CHURN'] = data2['CHURN'].map({'STAY':0, 'LEAVE' : 1})

model1 = Linear(data, 'y')
model1.linear_modeling_all()

model2 = Knn(data, 'y')
model2.scaling_mm()
model2.KNRegressor()

model3 = Knn(data2, 'CHURN')
model3.scaling_mm()
model3.KNClassifier()

model4 = Logistic(data2, 'CHURN')
model4.LogisticReg()


print('LinearRegression')
print(model1.model.coef_)
print(model1.model.intercept_)
print(model1.r_squared())
print(model1.rmse())
print(model1.mae())
print(model1.mape())
print('*'*30)
print('KNeighborsRegressor')
print(model2.r_squared())
print(model2.rmse())
print(model2.mae())
print(model2.mape())
print('*'*30)
print('KNeighborsClassifier')
print(model3.conf_matrix())
print(model3.classif_report())
print(model3.accuracy())
print(model3.recall())
print('*'*30)
print('LogisticRegression')
print(model4.model.coef_)
print(model4.model.intercept_)
print(model4.conf_matrix())
print(model4.classif_report())
print(model4.accuracy())
print(model4.recall())