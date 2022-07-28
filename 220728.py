# 실습1
def electricPay(kwh):
    basic_pay = 410
    use_pay = kwh * 60.7
    
    if kwh >= 100:
        basic_pay += 500
        use_pay += (kwh-99) * (125.9 - 60.7)
        
    if kwh >= 200:
        basic_pay += 690
        use_pay += (kwh-200) * (187.9 -125.9)
    
    pay = basic_pay + use_pay
    return int(pay*1.1 + pay*0.037)
    
print(electricPay(250))

# 실습2
def plus_minus(count):
    result = ''
    
    for i in range(count):
        if i % 2 == 0:
            result += '+'
        else:
            result += '-'
    
    return result

print(plus_minus(12))

# 실습3
def skip_num(st, end, skipNum):
    for i in range(st, end+1):
        if i != skipNum:
            print(i, end=' ')
    else:
        print()

skip_num(1,12,8)

# 실습4
def squared(num):
    for i in range(2, 6):
        if num ** (1/i) == int(num ** (1/i)):
            print(int(num ** (1/i)), i)

squared(36)
    
# 추가 실습0
def solution0(a, b):
    answer = 1
    while b > 0:
        a, b = b, a % b
    
    return a

print(solution0(4,6))

# 추가 실습1
def solution1(a, b):
    answer = 1
    
    return a * b / solution0(a, b)

print(solution1(60,48))

# 추가 실습2
def solution2(n):
    count = 0
    strN = str(n)
    if n < 10:
        strN = '0' + str(n)
    
    while True:
        count += 1
        
        a = strN[1]
        b = int(strN[0]) + int(strN[1])
        c = str(b)
        if b >= 10:
            c = c[1]
            
        if n == int(a+c):
            break
        else:
            strN = a+c
    # 참고
    # while True:
    #     a = n //10
    #     b = n % 10
    #     sumab = a+b
    #     i = (b * 10) + (sumab % 10)
        
    return count

print(solution2(int(input())))


# 추가 실습3
def solution3(left, right):
    answer = 0
    
    for i in range(left, right+1):
        if i ** 0.5 == int(i ** 0.5):
            answer -= i
        else:
            answer += i
    
    return answer

print(solution3(13,17))

# 추가 실습4
def solution4(num):
    result = []
    for i in num:
        result.append(i)
        if i == '0' or i == '1':
            result.append('+')
            if len(result) >= 3:
                result[-3] = '+'
        else:
            result.append('*')
            
    else:
        del result[-1]
        print(''.join(result))
        
    
    return eval(''.join(result))

print(solution4('02984'))
print(solution4('1205815'))
print(solution4('567'))

# 추가 실습5
def solution5(n):
    result = ''
    left = [int(i) for i in n[:len(n)//2]]
    right = [int(i) for i in n[len(n)//2:]]
    
    if sum(left) == sum(right):
        result = 'LUCKY'
    else:
        result = 'READY'
        
    return result
    
print(solution5('123402'))
print(solution5('7755'))
    
# 추가 실습6
def solution6(n):
    
    if n ** 0.5 == int(n ** 0.5):
        return (int(n ** 0.5) + 1) ** 2
    else:
        return -1
    
print(solution6(121))
print(solution6(3))


