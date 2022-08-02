import numpy as np

# hanky74@datainsight.biz

### 파이썬 기초
# 1) range()를 사용하여, 100이하의 수 중, 7의 배수를 리스트 a 에 담으시오.
a = [i*7 for i in range(1,(100//7) + 1)]
# a = [i*7 for i in range(7, 101, 7)]
print(a)

# 2) a에서 인덱스 4~ 7까지 조회하시오.
print(a[4:8])

# 3) a에서, 끝에서 세번째 값을 조회하시오.
print(a[-3])
    
# 4) a에 데이터 갯수(길이)는?
print(len(a))

# 5) a 값들의 합과 평균을 구하시오.
print(sum(a))
print(sum(a) / len(a))

# 6) 반복문을 이용하여 100이하의 소수(prime number)를 리스트에 담아 봅시다.
# * 소수(prime number) : 약수가 오직 1과 자기자신 만 존재하는 수. 
def q6():
    prime_num = [0 for i in range(101)]
    prime = []
    for i in range(2, 101):
        if prime_num[i] == 0:
            prime_num[i] = i
            prime.append(i)
            for j in range(i+i, 101, i):
                prime_num[j] = -1
    
    return prime

print(q6())


# 7) 아래 값으로 딕셔너리 d를 생성해 봅시다.

# |key | value|
# |----|----|
# |v1 | [1,2,3]|
# |v2 | {'a':23, 'b':[4,5]}|

d = {'v1' : [1,2,3], 'v2' : {'a':23, 'b':[4,5]}}
print(d)

# 8) d에서 [1,2,3]을 출력해 봅시다.
print(d['v1'])

# 9) d에서 23을 출력해 봅시다.
print(d['v2']['a'])

# 10) d에서 5를 출력해봅시다.
print(d['v2']['b'][1])

# 11) d에 key 'newKey' , value (1,2) 를 추가하고 출력해봅시다.
d['newKey'] = (1,2)
print(d['newKey'])


### Numpy 기초 - 숫자 타입

a = np.array([10, 11, 12, 13, 14, 15])
print('----------a----------')
print(a)
print(type(a))
print(a.ndim)
print(a.shape)
print(a.dtype)
print(a[0])
print(a.size)
print()


b = np.array([[11, 12, 13, 14], 
              [15, 16, 17, 18], 
              [1.9, 20, 21, 22]])

print('----------b----------')
print(b)
print(type(b))
print(b.ndim)
print(b.shape)
print(b.dtype)
print(b[0])
print(b.size)
print(b.reshape(2,6))
print(b[[i for i in range(0,3,2)]])
print(b[[0, 1, 2],[0, 1, 0]])
print()

c = np.array([[[1,2,3],[4,5,6]],
              [[7,8,9],[0,1,2]]])

print('----------c----------')
print(c)
print(c.reshape(-1, 4,3))
print()


# 배열 만들기
a = np.array([[11, 12, 13, 14], 
              [15, 16, 17, 18], 
              [19, 20, 21, 22]])

# 배열 형태 확인
print(a)

# (4, ?))형태의 2차원 배열
print(a.reshape(4,-1))

# (2, ?) 형태의 2차원 배열
print(a.reshape(2,-1))

# np.eye()
print(np.eye(9))

# np.full()
print(np.full((2,2), 'a'))

# numpy 인덱스
test = np.array([[11, 12, 13, 14], 
                 [15, 16, 17, 18], 
                 [19, 20, 21, 22]])

print(test[1,1]) # 16
print(test[2]) # a[2,:] / 19 20 21 22
print(test[:,2]) # 13 17 21
print(test[[1,2],[1,3]]) # 16 22
print()

# numpy 슬라이싱
test2 = np.array([[11, 12, 13, 14], 
                  [15, 16, 17, 18], 
                  [19, 20, 21, 22]])

print(test2[:,1:2]) # test2[:,1] - 1차원 표현 / test[:,[1]] - 2차원 표현
print(test2[:,1])
print(test[:,[1]])
print(test2[1:3,1:3])

# numpy 조건
score= np.array([[78, 91, 84, 89, 93, 65],
                 [82, 87, 96, 79, 91, 73]])

print(score)
# 90 이상
print(score[score >= 90])
over90 = score >= 90
print(score[over90])
# 80미만
print(score[score < 80])
# 짝수
print(score[score % 2 == 0])

# numpy 배열 연산
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

# 확인
print(x)
print(y)

# +
print(x+y)
print(np.add(x,y))
# -
print(x-y)
print(np.subtract(x,y))
# *
print(x*y)
print(np.multiply(x,y))
# /
print(x/y)
print(np.divide(x,y))
# **
print(x ** y)
print(np.power(x, y))
# //
print(np.sqrt(x))


# 배열 집계 sum, max, min, mean, std
a = np.array([[1,5,7],[2,3,8]])

# 전체 집계
print(np.sum(a))
# 열기준 집계
print(np.sum(a, axis = 0))
# 행기준 집계
print(np.sum(a, axis = 1))


# argmax : 가장 큰 값의 인덱스 / argmin : 가장 작은 값의 인덱스
print(np.argmax(a))
# 행 방향 최대값의 인덱스
print(np.argmax(a, axis = 0))
# 열 방향 최대값의 인덱스
print(np.argmax(a, axis = 1))

# np.where(조건, 참, 거짓)
print(np.where(a > 3, 1, 0))
print(np.where(a > 3, a, 0))

# np.linspace(시작, 끝, 사이값, 개수)
print(list(range(1,11,2)))
print(np.linspace(0,10,20))


### 종합실습
np_arr = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9],
                   [10,11,12]])
# 행/열
print(np_arr.shape)
# 배열변경
re_np_arr = np_arr.reshape(3,-1)
print(re_np_arr)
# 3행
print(np_arr[2])
# 요소 * 10
print(np_arr * 10)
# [8 9 10 11 12] 출력
print(np_arr[np_arr > 7])
# [8 9 10 11 12] * 2
# np_arr[np_arr > 7] *= 2
np_arr = np.where(np_arr > 7, np_arr * 2, np_arr)
print(np_arr)
# 3배수 0 / 1
np_zero = np.where(np_arr % 3 == 0, 1, 0)
print(np_zero)
# np_arr 평균
print(np.mean(np_arr))
print(np.mean(np_arr, axis=0))
print(np.mean(np_arr, axis=1))

