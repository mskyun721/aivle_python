import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import *
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

# Linear, Logistic
from sklearn.linear_model import LinearRegression, LogisticRegression

# knn
from knn import KNeighborsClassifier, KNeighborsRegressor

# decision
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor

# svm
from sklearn.svm import SVC, SVR

# bagging
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

# boosting
from xgboost import XGBClassifier, XGBRegressor


### 분류모델
# data
data_path = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/Carseats.csv'
data = pd.read_csv(data_path)
data.shape

# data preprocessing
data['Diff_Price'] = data['CompPrice'] - data['Price']
data.drop('CompPrice', axis = 1, inplace = True)

target = 'Sales'
x = data.drop(target, axis=1)
y = data[target]

data.info()
dumy_col = ['ShelveLoc', 'Urban', 'US', 'Education']
x = pd.get_dummies(x, columns=dumy_col, drop_first=True)

x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.3)

# scaling
scaler = MinMaxScaler()
x_train_s = scaler.fit_transform(x_train)
x_val_s = scaler.fit_transform(x_val)

# param
k = int(y_val.count() ** 0.5)

params = {
    'model_logitic' : {

    }
    , 'model_knnc' : {
        'n_neighbors' : range(1, k+6)
        , 'metric': ['euclidean', 'manhattan']}
    ,'model_dec' : {
        'max_depth' : range(1,11)
        , 'min_samples_leaf': [20,30,50,70,100]
    }
    ,'model_svm' : {
        'C': range(1,11)
        , 'gamma' : np.linspace(0.01,1,20)
    }
    ,'model_ran' : {
        'max_features' : range(1, x_train.shape[1] + 1)
        , 'n_estimators' : range(10,151,10)
    }
    ,'model_xgb' : {
        'max_features' : range(1, x_train.shape[1] + 1)
        , 'n_estimators' : range(10,151,10)
    }
}

# model
model_logitic = LogisticRegression()

model_knnc = KNeighborsClassifier()
model_dec = DecisionTreeClassifier()
model_svm = SVC()
model_ran = RandomForestClassifier()
model_xgb = XGBClassifier()
model = {'model_logitic':model_logitic, 'model_knnc':model_knnc, 'model_dec':model_dec, 'model_svm':model_svm, 'model_ran':model_ran, 'model_xgb':model_xgb}

# GridSearch
grid = GridSearchCV()
