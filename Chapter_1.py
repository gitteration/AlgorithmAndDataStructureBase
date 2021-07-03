## 알고리즘이란 : 문제를 해결하기 위한 일련의 절차 


### 1
# 세 정수의 최댓값 구하기
a = int(input('정수 a의 값 입력 : '))
b = int(input('정수 b의 값 입력 : '))
c = int(input('정수 c의 값 입력 : '))

maximum = a

if b > maximum : maximum = b
if c > maximum : maximum = c

print(f'최대값은 {maximum}')


# print 구문안에 f 또는 F를 붙여 문자열을 작성하면 { } 사이의 변수 또는 리터럴 값을 참조하여 표현할 수 있다.
# 이렇게 순서대로 진행되는 구조를 순차 구조라고 한다.
# if문의 조건식에 따라 실행 흐름이 변경되는 구조를 선택 구조 라고 한다.
# 파이썬의 if문은 if문과 : 사이가 조건식이며 문장 끝에 ; 을 붙이지 않는다.
# int 자료형은 10진수 정수형이다.

### 2
# 10진수란 우리가 평소에 사용하는 진수이다. 우리는 숫자를 0~9까지 표현하지만 컴퓨터는 0과 1만 표현을 하는데 이를 2진수라고 한다.
# 10진수에서 2 or 8 or 16 진수를 변환하는 계산법은 소인수분해와 비슷하다. 구글링해보면 많은 자료들이 나오니 까먹으면 다시 찾아보자  
number = int(input('10진수에서 2진수,8진수,16진수로 변환할 숫자를 입력 : '))
b = bin(number)
o = oct(number)
h = hex(number)

print(f'입력한 숫자의 2 진수는 : {b}')
print(f'입력한 숫자의 8 진수는 : {o}')
print(f'입력한 숫자의 16 진수는 : {h}')

# 문자열을 정수로 형 변환
int('17') # 10진수 정수형으로 변환(기본)'
int('0b110', 2) # 2진수 문자열을 10진수 정수형으로 변환 int(진수값, 진수)

### 3
# 문자열과 숫자 입력받기
print('문자열 입력 : ', end='')
str = input()
print(f'입력한 문자열은 {str} 입니다.')

# 위의 로직을 더 간단하게 하자면

str = input('문자열 입력 : ')
print(f'입력한 문자열은 {str} 입니다.')

### 4

# a,b,c 정수의 중앙값 구하기(정수들을 크기순으로 정렬했을 시 가장 중앙에 위치하는 값을 의미)
#4-1
def med(a,b,c):
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
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    return c

print('세 변수의 중앙값을 구합니다.')
a = int(input('a의 값 : '))
b = int(input('b의 값 : '))
c = int(input('c의 값 : '))
print(f'4-1의 중앙값은{med(a,b,c)}이다.')
print(f'4-2의 중앙값은{med2(a,b,c)}이다.')
# 4-1과 4-2는 같은 로직이다. 4-2가 코드는 짧지만 효율성에는 안좋다. 첫 번째 elif문에서 불필요하게 한번 더 수행하기 때문이다.









