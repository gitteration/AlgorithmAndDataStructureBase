### 4

# a,b,c 정수의 중앙값 구하기(정수들을 크기순으로 정렬했을 시 가장 중앙에 위치하는 값을 의미)

#4-1
def med(a,b,c):
    # a = 1, b = 2, c = 3
    if a>=b:
        if b>=c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a>c:
        return a
    elif b>c:
        return c
    else:
        return b

# 4-2
def med2(a,b,c):
    # a = 1, b = 2 , c = 3
    #    true  and  fals   or  false  and false = false
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    #      false and false or  true  and true  = true
    elif (a > b and c < b) or (a < b and c > b):
        return b
    return c

# 4-1과 4-2는 같은 로직이다. 4-2가 코드는 짧지만 효율성에는 안좋다. 첫 번째 elif문에서 불필요하게 한번 더 수행하기 때문이다.

print('세 변수의 중앙값을 구합니다.')
a = int(input('a의 값 : '))
b = int(input('b의 값 : '))
c = int(input('c의 값 : '))
print(f'4-1의 중앙값은{med(a,b,c)}이다.')
print(f'4-2의 중앙값은{med2(a,b,c)}이다.')






