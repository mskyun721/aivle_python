import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


path = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/retail_demand2.csv'
data = pd.read_csv(path, usecols = ['date','sales', 'comp_sales', 'tot_sales'])

data = data.loc[data['date']>= '2017-12-01'].reset_index(drop = True)

data['date'] = pd.to_datetime(data['date'])

data['tot_sales'] = data['tot_sales'] / 5

data.columns = ['date','item1', 'item2', 'item3']

print(data.head(10))

# 차트 그리기
plt.plot(data['item1'])
plt.show()

# 날짜 축으로 sales에 대해 라인차트를 그려봅시다.
plt.plot('date', 'item1', data = data)
# == plt.plot(data['date'], data['item1'])
plt.show()

### 연습문제
plt.plot(data['item3'])
plt.show()

x = [1,2,3,4,5,6,7,8,9,10]
y = [2,5,7,8,5,6,4,8,7,6]
plt.plot(x, y)
plt.show()