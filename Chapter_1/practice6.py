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