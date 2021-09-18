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

def med2(number) :
    sum = 0 
    for i in range(1, number+1):
        print(i)
        sum += i
    return sum
print('1부터 n까지의 정수의 합 구하기(for)')
number = int(input('값을 입력해주세요:'))
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

# 이 소스의 코드의 문제는 만약 입력한 n값이 1000번이라 한다면 1000번의 if문을 실행하는 것 이다.
for i in range(n):
    if i % 2:
        print('-', end='')
    else:
        print('+', end='')
print()
# 바로 위의 소스의 개선버전이다. 
# n / 2를 하여 나머지 만큼 반복을 하고 마지막 if문으로 나머지를 구하여 마지막 문장을 출력해준다.
# 언더바(_)의 의미는 반환하는 인덱스가 필요하지 않을 때 무시용으로 사용한다
for i in range(n // 2):
    print('+-', end ='')
if n % 2 :
    print('+', end='')
