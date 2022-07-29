# 미니실습1
def min_of(arr):
    # minimum = arr[0]
    
    # for i in range(1, len(arr)):
    #     if minimum > arr[i]:
    #         minimum = arr[i]
        
    return min(arr)

t = (4,7,5.6,2,314,1)
s = 'string'
a = ['dts','aac','flac']

# print(min_of(t))
# print(min_of(s))
# print(min_of(a))

# 미니실습2
def list_reverse(arr):
    arr.reverse()
    
    # for i in range(len(arr) // 2):
    #     arr[0+i], arr[-1-i] = arr[-1-i], arr[0+i]
        
    return arr

# print(list_reverse([1,2,3,4,5]))

# 미니실습3
def seq_search(arr, key):
    i = 0
    ifcount = 0
    while True: 
        ifcount += 1
        if i == len(arr):
            
            break
            # return -1
        ifcount += 1
        if arr[i] == key:
            
            break
            # return i
        i += 1
        
    return ifcount

def seq_search_sentinel(arr, key):
    a = arr.copy()
    a.append(key)
    i=0
    ifcount = 1
    while True:
        ifcount += 1
        if a[i] == key:
            
            break
        i += 1
    
    # return -1 if i == len(arr) else i
    return ifcount
        

a = [2, 5, 1, 3, 9, 6, 7] 
# print(seq_search(a, 7))
# print(seq_search_sentinel(a, 7))

# 이진검색
def bin_search(arr, key):
    st = 0
    ed = len(a)-1
    
    while True:
        mid = (st + ed) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            st = mid + 1
        else:
            ed = mid - 1
        
        if st > ed:
            break
        
    return -1


# 실습1
def primeNum(st, ed):
    list_prim = [0 for i in range(ed+1)]
    
    for i in range(2, ed+1):
        if list_prim[i] == 0:
            list_prim[i] = i
            
            for j in range(i+i, ed+1, i):
                list_prim[j] = -1

    list_prim = [i for i in list_prim[st:] if (i != 0 and i != -1)]
    return list_prim

# print(primeNum(2,1000))

# 실습2
def list_reverse2():
    reverse = []
    while True:
        a = input()
        
        if a == '':
            break
        
        reverse.insert(0,a)
    
    return reverse

# print(list_reverse2())

# 실습3
def list_search(arr, find):
    
    if find in arr:
        return arr.index(find)
    else:
        return -1
    
    
# a = list(input().split())
# b = input()
# print(list_search(a, b))

# 실습4
def find_max_min(arr):
    return arr.index(max(arr)), arr.index(min(arr))
    
# print(find_max_min([1,3,2,4,5,9,8,6]))


# 추가실습0
def search_low_num(lowNum, num_arr):
    result = 0
    
    for i in num_arr:
        if result == (lowNum - 1):
            print()
            break
        
        if i < lowNum:
            print(i, end=' ')
            result+= 1
    
# n, x = map(int, input().split())
# arr = list(map(int, input().split()))

# search_low_num(x, arr)


# 추가실습1
def lotto(my, win):
    rate = [6,6,5,4,3,2,1]
    
    zeroCount = my.count(0)
    match = [i for i in my if i in win]
    matchCount = len(match)
    
    # right = list(filter(lambda x: x in win, my))
    # zeros = list(filter(lambda x: x == 0, my))
    
    return [rate[zeroCount + matchCount], rate[matchCount]]

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
# print(lotto(lottos, win_nums))


# 추가실습2
def zero_nine(nums):
    
    return int((9*10/2) - sum(nums))

arr = [1,2,3,4,6,7,8,0]
# print(zero_nine(arr))


# 추가실습3
# 컴퓨터 매장에는 n개의 부품이 있으며, 부품마다 정수 형태의 고유한 번호가 있다. 
# 매장에 부품 재고가 있는지 확인하는 프로그램을 작성하라. 
# 매장이 가지고 있는 부품 리스트와 고객이 확인하고자 하는 부품 리스트를 입력받는다. 
# 고객이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes, 없으면 no를 출력한다. 
# 제한사항
# - 부품 재고의 갯수는 고려하지 않으며 부품이 있는지 여부만 체크한다
# - 부품 리스트 길이(n, m)는 1이상, 15이하입니다.
# - 매장 보유 부품 번호는 오름차순으로 정렬된 형태로 입력한다.
# - 부품 리스트의 원소는 100 이하인 자연수입니다.

def comStore(store, customer):
    answer = ['yes' if i in store else 'no' for i in customer]
    
    return answer

# https://github.com/sanghas/kt_aivle_python
def solution(store, customer):
    mum = store[len(store)-1]
    if max(customer) > mum:
        mum = max(customer)
    _list = [0]*(mum+1)
    for i in store:
        _list[i] = 1
    ans = []
    for i in customer:
        if _list[i] :
            ans.append('yes')
        else :
            ans.append('no')
    return ans

# def bin_search(a, key):
#     pl = 0
#     pr = len(a)-1
    
#     while True:
#         pc = (pl + pr) // 2
#         if a[pc] == key:
#             return pc
#         elif a[pc] < key:
#             pl = pc + 1
#         else:
#             pr = pc - 1
        
#         if pl > pr:
#             break
    
#     return -1

# def solution(store, customer):
    
#     answer = []
    
#     for i in customer:
#         result = bin_search(store,i)
#         if result != -1:
#             answer.append('yes')
#         else:
#             answer.append('no')
            
#     return answer

store = [2,3,7,8,9]
customer = [7,5,9]
# print(comStore(store, customer))
    


# 추가실습4
# 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다.
# 예를 들어 2와 7의 최소공배수는 14가 됩니다. 
# 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. 
# n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
# 제한 사항
# - arr은 길이 1이상, 15이하인 리스트입니다.
# - arr의 원소는 100 이하인 자연수입니다.

# 최소공배소
import copy

def lcm(a, b):
    c = a*b
    
    while b > 0:
        a, b = b, a % b
        
    return int(c / a)
    
def lcm_multi(arr):
    while len(arr) != 1:
        arr.append(lcm(arr.pop(), arr.pop()))
        
    return arr[0]

# def solution(arr):
    
#     maximum = 0
#     for i in range(len(arr)):
#         if arr[i] > maximum:
#             maximum = arr[i]
    
#     mul = 1
#     for i in range(len(arr)):
#         mul = mul * arr[i]
            
#     for i in range(maximum,mul+1):
#         flag = 0
#         for j in range(len(arr)):
#             if i%arr[j] == 0:
#                 flag += 1
        
#         if flag == len(arr):
#             answer = i
#             break
    
#     return answer

arr = [2,6,8,14]
# print(lcm_multi(arr))


# 추가실습5
def plus_multi(s):
    answer = []
    count = s // 2

    if s == 1:
        return [-1]
    
    if s % 2 != 0:
        answer = [count, count+1]
    else:
        answer = [count, count]
    
    return answer

s = 11
print(plus_multi(s))

# 추가실습6
def del_min(arr):
    if len(arr) == 1:
        return 1
    
    idx_min = arr.index(min(arr))
    del arr[idx_min]
        
    return arr

arr = [4, 3, 2, 1]
# print(del_min(arr))

# 추가실습7
def non_overlap(arr):
    setArr = list(set(arr))
    setArr.sort()

    return setArr

arr = [1,1,3,3,0,1,1]
#arr = [4,4,4,3,3]
# print(non_overlap(arr))