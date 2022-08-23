import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# knn model
from sklearn.linear_model import LogisticRegression

# metrics
from sklearn.metrics import *

# train/val/test
from sklearn.model_selection import train_test_split


class Logistic:
    def __init__(self, df, target, feature=[]):
        self.x = df.drop(target, axis=1)
        self.y = df[target]
        if feature:
            self.x = self.x[feature]
        self.x_train, self.x_val, self.y_train, self.y_val = train_test_split(self.x, self.y, test_size=.3)
    
    def LogisticReg(self, ):
        self.model = LogisticRegression()
        self.model.fit(self.x_train, self.y_train)
        self.pred = self.model.predict(self.x_val)

    def conf_matrix(self, ):
        return confusion_matrix(self.y_val, self.pred)
    
    def classif_report(self, ):
        return classification_report(self.y_val, self.pred)

    def accuracy(self, ):
        return accuracy_score(self.y_val, self.pred)
    
    def recall(self, ):
        return recall_score(self.y_val, self.pred)