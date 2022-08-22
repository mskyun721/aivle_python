import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import *

class default_modeling:
    def __init__(self, df, target):
        self.model = LinearRegression()
        self.x = df.drop(target, axis=1)
        self.y = df[target]
        self.x_train, self.x_val, self.y_train, self.y_val = train_test_split(self.x, self.y, test_size=.3)
        
    def linear_modeling_all(self, ):
        self.model.fit(self.x_train, self.y_train)
        self.pred = self.model.predict(self.x_val)
        self.y_val_mean = self.y_val.mean()

    def linear_modeling_feature(self, features):
        self.x_train = self.x_train[features]
        self.x_val = self.x_val[features]

    def r_squared_sst(self, ):
        self.sst = np.sum(np.power(self.y_val - self.y_val_mean, 2))

        return self.sst

    def r_squared_sse(self, ):
        self.sse = np.sum(np.power(self.y_val - self.pred, 2))
        
        return self.sse
    
    def r_squared_ssr(self, ):
        self.ssr = np.sum(np.power(self.pred - self.y_val_mean, 2))
        
        return self.ssr

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