### 반복문 

# while문
def med(number) :
    i = 1
    sum = 0
    while i <= number:
        sum += i
        i += 1   
    return sum 
print('1부터 n까지의 정수의 합 구하기(while)')
number = int(input('값을 입력해주세요:'))
print(f'1부터 {number}까지 정수의 합은 {med(number)}')

# for문 
# 변수가 하나만 있을 경우에는 for문을 사용하는것이 낫다.
# range(start, stop) - start부터 stop미만까지 

print('1부터 n까지의 정수의 합 구하기(for)')
while True : 
    number = int(input('값을 입력해주세요:'))
    if number > 0 :
        break
    else : print('1 이상 입력해주세요')
def med2(number) :
    sum = 0 
    for i in range(1, number+1):
        print(i)
        sum += i
    return sum
print(f'1부터 {number}까지의 정수의 합은 {med2(number)}')

# 가우스 덧셈 
# for문을 이용하지않고 합을 구할 수 있음
# //는 몫 연산자라고 하며 나눈 몫을 구해주고 %는 나머지 연산자로 나눈 나머지를 구해준다.
print('1부터 n까지의 정수의 합 구하기(가우스 덧셈)')
number = int(input('값을 입력해주세요:'))
sum = number * (number+1) // 2
print(f'1부터 {number}까지의 정수의 합은 {sum}')

# a부터 b까지 정수의 합 구하기(for)
print('a부터 b까지 정수의 합 구하기')
a = int(input('정수 a를 입력 : '))
b = int(input('정수 b를 입력 : '))
sum = int(0)
if(a>b):
    a, b = b, a

for i in range(a, b+1):
    sum += i
print(f'{a}부터 {b}까지의 정수의 합은 {sum} 입니다')

# 튜플이란 ? 파이썬의 리스트와 비슷하다. 즉, 변수의 값들을 교환할 때 사용한다
str1 = 'java'
str2 = 'javscript'
print(f'str1의 value는 {str1} 이고 str2의 value는{str2} 이다')
str1 , str2 = str2 , str1
print(f'값 교환 - str1의 value는 {str1}로 변경되었고 str2의 value는 {str2}로 변경되었다')

# +와 -를 번갈아 출력하기
# print문의 end는 출력을 완료한 후 뒤에 문자열을 추가하는 옵션이다. 빈 문자열로 삽입한 이유는 개행을 막기위함(기본적으로 print문이 끝나면 개행이 되기 때문이다.)
print('+와-를 번걸아 출력하기')
n = int(input('출력할 횟수 입력 : '))
for i in range(n):
    if i % 2:
        print('-', end='')
    else:
        print('+', end='')
print()
# 이 소스의 코드의 문제는 만약 입력한 n값이 1000번이라 한다면 1000번의 if문을 실행하는 것 이다.

# 바로 위의 소스의 개선버전이다. 
# n / 2를 하여 나머지 만큼 반복을 하고 마지막 if문으로 나머지를 구하여 마지막 문장을 출력해준다.
# 언더바(_)의 의미는 반환하는 인덱스가 필요하지 않을 때 무시용으로 사용한다
for i in range(n // 2):
    print('+-', end ='')
if n % 2 :
    print('+', end='')
print()

# *를 n개 출력하되 w개마다 줄바꿈하기 
print('*를 n개 출력하되 w개마다 줄바꿈하기')
a = int(input('출력할 a개 입력:'))
b = int(input('줄바꿈 b개 입력:'))

'''
 for i in range(a):
    print('*', end = '')
    if i % b == b-1 : print()    
'''
# 이 로직은 for문 돌 때마다 if문이 실행되므로 비효율적이다.

for _ in range(a // b):
    print('*' * b)
rest = a % b
if rest:print('*' * rest)
# 이 로직은 a // b 나눈 값 만큼 for문을 반복하고 마지막은 나머지를 사용하여 처리한다.

area = int(input('직사각형의 넓이를 입력 : '))
for i in range(1, area + 1) : 
    if i * i > area : break
    if area % i : continue
    print(f'{i} x {area // i}')  


# 난수 n개 생성하기
import random
print('난수 n개 생성하기')
n = int(input('난수를 생성할 n개 입력 : '))
for _ in range(n) :
    random_number = random.randint(10, 99)
    print(random_number, end = ' ')
    if random_number == 13 : 
        print('\n13에 걸렸으므로 프로그램 중단')
        break
else : 
    print('\n난수 생성을 종료')
# for문의 else문을 사용하여 반복이 끝나면 else문으로 빠진다

# 1~10까지 5을 제와하고 출력하기
for i in range(1, 13) : 
    if i == 5 :  
        continue 
    print(f'{i}' ,end = ' ')
print()
# 이 로직도 비효율적이다. 만약 99999번을 반복한다면 if문이 그만큼 실행되기 때문이다.

# 2자리 양수 입력받기
while True : 
    n = int(input('2자리 양수 입력(10~99사이) : '))
    if(n >= 10 and n <= 99) : 
        break

print(f'입력한 값은 {n} 입니다')
# if문을 n >= 10 and n <= 99 대신 10 <= n <= 99으로 변경할 수 있다.

# 다중 for 문
# {i * j:3}에서 식:숫자는 숫자만큼 자리 수로 출력해준다 
print('-' * 27)
for i in range(1,10) :
    for j in range(1,10) :
        print(f'{i * j:3}', end = '')
    print()
print('-' * 27)

# 직각인 이등변 삼각형 별찍기
n = int(input('짧은 변 입력(직각인 이등변 삼각형) : '))
for i in range(n+1) : 
    for j in range(i) :
        print('*', end='')
    print()

# 오른쪽 아래가 직각인 이등변 삼각형 별찍기
# 두 로직 중 어느게 빠른지 측정해보자(9999번 찍어보기) 
# 첫 번째 로직 71초, 두 번째 로직 65초, 추가적으로 js는 44초
import time
start_time = time.time()
n = int(input('짧은 변 입력(오른쪽 아래가 직각인 이등변 삼각형) : '))

'''
for i in range(n) : 
    for j in range(n+1) :
        if j < n-i :
            print(' ', end='')
        else :
            print('*', end='')
    print()
print("종료시간 : ", time.time() - start_time)  
'''

for i in range(n) : 
    for _ in range(n-1-i) :
        print(' ', end = '')
    for _ in range(i+1) : 
        print('*', end = '')
    print()
print("종료시간 : ", time.time() - start_time) 
