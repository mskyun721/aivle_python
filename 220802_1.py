import pandas as pd
import numpy as np

data = pd.read_csv('csv/airquality_simple.csv')

print(data)
print(data.shape)
print(data.loc)
print(data.dtypes)
print(data.describe())


path = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/Attrition_simple2.CSV'
data = pd.read_csv(path)

print(data.head()) # default 5
print()
# data.PercentSalaryHike
print(data['PercentSalaryHike'])
print()
print(data[['Age', 'DistanceFromHome', 'Gender']])
print()
print(data[['Age', 'DistanceFromHome', 'Gender']].sort_values(by='DistanceFromHome', ascending=False))
print()

# 조건 : .loc[행조건, 열이름] / numpy 비교 / 2개 이상 조건 시 ()로 묶어서 표현
print(data.loc[data['DistanceFromHome'] > 10])
print()
print(data.loc[(data['DistanceFromHome'] > 10) & (data['JobSatisfaction'] == 4)])
print()
# isin() : 원하는 값의 데이터만 조회
print(data.loc[data['JobSatisfaction'].isin([1,4])])
print()
# between : 원하는 값의 범위 조회
print(data.loc[data['Age'].between(25,30)])
print()
print(data.loc[(data['Age'].between(25,30)) & (data['JobSatisfaction'].isin([1,4]))])


### 종합실습
ti = pd.read_csv('https://raw.githubusercontent.com/DA4BAM/dataset/master/titanic_simple.csv')

print(ti['Name'])
print()
print(ti[['Name', 'Age', 'Sex']])
print()
# same
# print(ti.loc[:, ['Name', 'Age', 'Sex']])
# print(ti.loc[0:9, ['Name', 'Age', 'Sex']])
print(ti[['Name', 'Age', 'Sex']].head(10))
print()
print(ti.loc[ti['Age'] >= 70])
print()
Fare_mean = ti['Fare'].mean()
print(Fare_mean)
print()
print(ti.loc[ti['Fare'] < Fare_mean, ['Name']])
print()
print(ti.loc[ti['Embarked'].isin(['Southhampton', 'Queenstown'])])
print()
print(ti.loc[ti['Age'].between(10,19) & ti['Sex'].isin(['male']), ['Fare']].mean())
print()
print(ti['Fare'].loc[ti['Age'].between(10,19) & ti['Sex'].isin(['male'])].mean())


### 데이터 집계
path = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/Attrition_simple2.CSV'
data = pd.read_csv(path)  

# 상위 5개 확인
data.head(5)

print(data['MonthlyIncome'].sum())
print()
print(data[['MonthlyIncome', 'TotalWorkingYears']].mean())
print()
# as_index : True / False (default = True) | as_index = False : 무조건 dataFrame
print(data.groupby('MaritalStatus', as_index=False)['Age'].mean())
print()
print(data.groupby('MaritalStatus', as_index=False)[['Age','MonthlyIncome']].mean())
print()
print(data.groupby('MaritalStatus', as_index=False).sum())
print()
print(data.groupby(['MaritalStatus','Gender'], as_index=False)[['Age','MonthlyIncome']].mean())
print()
print(data.groupby('MaritalStatus')['MonthlyIncome'].agg(['min','max','mean']))
print()

### 연습문제
temp = pd.read_csv('https://raw.githubusercontent.com/DA4BAM/dataset/master/airquality_simple.csv')  

print(temp.info())
print()

print(temp.groupby('Month', as_index=False)[['Ozone', 'Wind', 'Temp']].mean())
print()
print(temp.groupby('Month')[['Ozone', 'Wind', 'Temp']].agg(['min','max','mean','std']))
print()

### 종합실습
ti = pd.read_csv('https://raw.githubusercontent.com/DA4BAM/dataset/master/titanic_simple.csv')

# 중앙값
print(ti[['Fare']].median())
print()
# Embarked 평균 Fare
print(ti.groupby('Embarked', as_index=False)[['Fare']].mean())
print()
# Embarked, Sex 평균 Fare, Age
tmp = ti.groupby(['Embarked', 'Sex'], as_index=False)[['Fare', 'Age']].mean()
print(tmp)
print()
# Pclass, survived별 Age, Fare의 최대, 최소, 평균, 표준편차
tmp2 = ti.groupby(['Pclass', 'Survived'], as_index=False)[['Age', 'Fare']].agg(['min','max','mean','std'])
print(tmp2)
print()
# print(tmp2.reset_index(inplace=True)) : 새로운 index 적용
# set_index : set_index(list, inplace=[True,False])
#               list - index로 사용할 columns
#               inplace - 새로운 index 적용 여부
print(tmp2.reset_index())
print()
# 탑승지역(Embarked)별, 나이 : 평균, 운임 : 최대값 
print(ti.groupby('Embarked').agg({'Age':'mean', 'Fare':'max'}))


### 데이터프레임 변경
# 데이터 읽어오기
path = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/Attrition_simple2.CSV'
data = pd.read_csv(path)  

# 열 이름 변경 
# inplace = True : 실제로 변경 시키는 코드
print(data.columns)
print(list(data.columns))
data.rename(columns={'DistanceFromHome' : 'Distance', 
                    'EmployeeNumber' : 'EmpNo',
                    'JobSatisfaction' : 'JobSat',
                    'MonthlyIncome' : 'M_Income',
                    'PercentSalaryHike' : 'PctSalHike',
                    'TotalWorkingYears' : 'TotWY'},
            inplace = True)

# 모든 열의 이름 변경 : 컬럼 수와 list len 불일치 시 에러
data.columns = ['Attr','Age','Dist','EmpNo','Gen','JobSat','Marital','M_Income', 'OT', 'PctSalHike', 'TotWY']

# 열 추가
# 전연도 income
data['LastYearIncome'] = round(data['M_Income'] / (1 + data['PctSalHike']/100))
# int로 타입 변환
data['LastYearIncome'].astype('int')
data['LastYearIncome'].apply(int)
print(list(data.columns))
data.rename(columns={'LastYearIncome':'LY_Income'},
            inplace=True)
print()

### 연습문제
print(data.value_counts('JobSat'))
print(data['JobSat'].value_counts())
print()
# isin() 가능
data['JobSat2'] = np.where((data['JobSat'] == 1) | (data['JobSat'] == 2), 'unsat', 'sat')
print(data[['JobSat','JobSat2']])
print()

data['Diff_Income'] = data['M_Income'] - data['LY_Income']
print(data[['M_Income', 'PctSalHike', 'LY_Income', 'Diff_Income']])
print()

# 데이터 csv 파일 저장
data.to_csv('csv/data_20220802.csv', index = False)

# 열 삭제
# axis = 0 : 행삭제, default / 1 : 열삭제
# inplace : 적용 여부
print(list(data.columns))
print()
data.drop('Diff_Income', axis=1, inplace=True)
print(list(data.columns))
print()
data.drop(['JobSat2', 'LY_Income'], axis=1, inplace=True)
print(list(data.columns))
print()

# map() : 범주형 값을 다른 값으로 변경
data['Gen'] = data['Gen'].map({'Male':1, 'Female':0})

data.drop(['PctSalHike', 'TotWY'], axis=1, inplace=True)
data['Marital'] = data['Marital'].map({'Single':0, 'Married':1, 'Divorced':2})
print(list(data.columns))
print(data[['Marital']])
print()

# cut() : 크기를 기준으로 범위를 나누어 등급을 지정
# 균등구간분할 : 범위 개수를 지정하여 자동으로 크기를 기준으로 나눈다.
data['Income_Group'] = pd.cut(data['M_Income'], 3, labels=['a','b','c'])
print(data['Income_Group'])
print(data.columns)
print()
print(data.groupby('Income_Group', as_index=False)['M_Income'].agg(['min','max']))
print()

# 등급 구하기
bin = [0, 10000, 15000, np.inf]
data['Income_Group2'] = pd.cut(data['M_Income'], bins=bin, labels=['a', 'b', 'c'])
# 범위 확인
print(data.loc(data['M_Income'] > 15000)[['M_Income','Income_Group2']])
print()



### 종합실습
path = 'https://bit.ly/TitanicFile'
ti = pd.read_csv(path)
print(list(ti.columns))
# PassengerId, Name, Ticket, Cabin 열을 한 번에 삭제하세요.
ti.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
# Sex 열 이름을 Male로 변경하세요.
ti.rename(columns={'Sex':'Male'},
          inplace=True)
# Male 열 값을 'male'은 1, 'female'은 0으로 변경하세요.
ti['Male'] = ti['Male'].map({'male':1, 'female':0})
# SibSp 열과 Parch 열의 값을 더한 결과를 갖는 Family 열을 추가하세요.
ti['Family'] = ti['SibSp'] + ti['Parch']
# SibSp, Parch 두 열을 삭제하세요.
ti.drop(['SibSp', 'Parch'], axis=1, inplace=True)
# 나이를 연령대로 구분하고자 합니다. 아래 조건의 값을 갖도록 변수를 추가하세요.
# bin(구간) + 1 = label(값)
age_list = list(range(0,90,10)) + [np.inf]
age_name = ['유아' if i == 0 else str(i)+'대' for i in age_list[:-1]]
print(ti[['Age']])
ti['AgeGroup'] = pd.cut(ti['Age'], age_list, False, age_name)
print(ti[['Age','AgeGroup']])
