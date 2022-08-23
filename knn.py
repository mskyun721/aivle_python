import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# scaling
from sklearn.preprocessing import *

# knn model
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier

# metrics
from sklearn.metrics import *

# train/val/test
from sklearn.model_selection import train_test_split


class Knn:
    def __init__(self, df, target, feature=[]):
        
        self.x = df.drop(target, axis=1)
        self.y = df[target]
        if feature:
            self.x = self.x[feature]
        self.x_train, self.x_val, self.y_train, self.y_val = train_test_split(self.x, self.y, test_size=.3)
    
    def scaling_mm(self, ):
        self.scaler = MinMaxScaler()
        self.x_train = self.scaler.fit_transform(self.x_train)
        self.x_val = self.scaler.fit_transform(self.x_val)
    
    def scaling_st(self, ):
        self.scaler = StandardScaler()
        self.x_train = self.scaler.fit_transform(self.x_train)
        self.x_val = self.scaler.fit_transform(self.x_val)

    def KNRegressor(self, k=5, metric='euclidean'):
        self.model = KNeighborsRegressor(n_neighbors=k, metric=metric)
        self.model.fit(self.x_train, self.y_train)
        self.pred = self.model.predict(self.x_val)
        
    def KNClassifier(self, k=5, metric='euclidean'):
        self.model = KNeighborsClassifier(n_neighbors=k, metric=metric)
        self.model.fit(self.x_train, self.y_train)
        self.pred = self.model.predict(self.x_val)

    ### KNRegressor
    def sst(self, ):
        self.sst = np.sum(np.power(self.y_val - self.y_val_mean, 2))

        return self.sst

    def sse(self, ):
        self.sse = np.sum(np.power(self.y_val - self.pred, 2))
        
        return self.sse
    
    def ssr(self, ):
        self.ssr = np.sum(np.power(self.pred - self.y_val_mean, 2))

    def r_squared(self, ):
        self.r2 = r2_score(self.y_val, self.pred)

        return self.r2

    def mse(self, ):
        self.mse_ = mean_squared_error(self.y_val, self.pred)

        return self.mse_

    def rmse(self, ):
        self.rmse_ = mean_squared_error(self.y_val, self.pred, squared=False)

        return self.rmse_

    def mae(self, ):
        self.mae_ = mean_absolute_error(self.y_val, self.pred)

        return self.mae_

    def mape(self, ):
        self.mape_ = mean_absolute_percentage_error(self.y_val, self.pred)

        return self.mape_
    
    ### KNClassifier
    def conf_matrix(self, ):
        return confusion_matrix(self.y_val, self.pred)
    
    def classif_report(self, ):
        return classification_report(self.y_val, self.pred)

    def accuracy(self, ):
        return accuracy_score(self.y_val, self.pred)
    
    def recall(self, ):
        return recall_score(self.y_val, self.pred)
