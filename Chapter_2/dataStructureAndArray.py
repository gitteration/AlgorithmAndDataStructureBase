'''
    파이썬의 배열은 리스트와 튜플로 구현할 수 있다.
    리스트와 튜플은 데이터 컨테이너라고 하며 원소를 변경할 수 있는지 없는지에 따라 차이가 있다.
'''
print('### 리스트 사용하기 ###')
##### 리스트 #####
# - 리스트는 뮤터블 리스트형 객체(원소를 자유롭게 추가,수정,삭제 가능)이다.
# 마지막 원소 뒤에 쉼표를 사용해도 상관없다

# [] 사용
list1 = []
list2 = [1,2,3]
list3 = ['a','b','c']

# list 함수 사용
list4 = list('abc')   # 각 문자로부터 원소 생성
list5 = list([1,2,3]) # 리스트로부터 원소 생성
list6 = list((1,2,3)) # 튜플로부터 원소 생성
list7 = list({1,2,3}) # 집합으로부터 원소 생성

# range 함수 사용
list8 = list(range(7))       # 0부터 7까지
list9 = list(range(3,8))     # 3부터 8까지
list10 = list(range(3,13,3)) # 마지막 인자값은 해당 값 만큼 더해서 생성한다.

# 원솟값이 없는 리스트 원하는 수 만큼 생성하기 
list11 = [None]*5

print(f'list1::: {list1}')
print(f'list2::: {list2}')
print(f'list3::: {list3}')
print(f'list4::: {list4}')
print(f'list5::: {list5}')
print(f'list6::: {list6}')
print(f'list7::: {list7}')
print(f'list8::: {list8}')
print(f'list9::: {list9}')
print(f'list10::: {list10}')
print(f'list11::: {list11}')

print('### 튜플 사용하기 ###')
##### 튜플 #####
# - 튜플은 원소 순서를 매겨 결합한 것으로 원소를 변경할 수 없는 이뮤터블 자료형이다.
# - 리스트와 같이 마지막 원소뒤에 쉼표를 사용해도 상관없다

# () 사용
tuple1 = ()
tuple2 = 1,     # 결합 연산자를 생략할 수 있다.
tuple3 = (1,)   
tuple4 = 1,2,3
tuple5 = 1,2,3,
tuple6 = (1,2,3)
tuple7 = (1,2,3,)
tuple8 = 'A','B','C'
# tuple2, tuple3 같이 1개의 원소만 생성할 경우 뒤에 쉼표를 붙여줘야한다. 

# tuple 함수 사용
tuple9 = tuple()
tuple10 = tuple('abc')
tuple11 = tuple([1,2,3])
tuple12 = tuple({1,2,3})
# range 함수 사용(리스트와 동일)
tuple13 = tuple(range(7))
tuple14 = tuple(range(3,8))
tuple15 = tuple(range(3,13,2))

print(f'tuple1::: {tuple1}')
print(f'tuple2::: {tuple2}')
print(f'tuple3::: {tuple3}')
print(f'tuple4::: {tuple4}')
print(f'tuple5::: {tuple5}')
print(f'tuple6::: {tuple6}')
print(f'tuple7::: {tuple7}')
print(f'tuple8::: {tuple8}')
print(f'tuple9::: {tuple9}')
print(f'tuple10::: {tuple10}')
print(f'tuple11::: {tuple11}')
print(f'tuple12::: {tuple12}')
print(f'tuple13::: {tuple13}')
print(f'tuple14::: {tuple14}')
print(f'tuple15::: {tuple15}')

print('### 언팩하기 ###')
# 리스트와 튜플 언팩하기
# - 언팩이란 리스트나, 튜플의 원솟값들을 풀어 여러 변수에 대입하는 것
x = [1,2,3]
a,b,c = x
print(a,b,c)

print('### 리스트 인덱스에 접근하기 ###')
# 특이하게 list에서 음수로도 접근이 가능하다
# - 양수에서는 맨 앞 인덱스가 0 부터 시작이지만 음수에서 맨 뒤에서 -1 부터 시작한다 
x = [1,2,3,4,5]
print(x[0], x[-5])
print(type(x[0]))
x[0] = 1.11 # 동적 타입이여서 기존 int형에서 float형으로 자동변환된다.
print(x[0])
print(type(x[0]))
# x[5] = 6 # 존재하지 않는 인덱스에는 값 할당이 안된다

print('### slice식으로 원소 접근하기 ###')
# 슬라이스식으로 원소에 접근하기
# - 기존 리스트나 튜플의 원소 일부를 일정한 간격으로 꺼내 새로운 리스트, 튜플로 만드는 것
# - s = [i:j:k] i는 시작할 인덱스, j는 종료 인덱스, k는 간격 
ori = [1,2,3,4,5]
s = ori[0:3]
print(s)
s = ori[0:5:2]
print(s)
s1 = ori[:] # 모두 출력
s2 = ori[3:] # 3인데스부터 끝까지 출력
s3 = ori[:3] # 3인덱스까지 출력
s4 = ori[::2] # 2 간격으로 모두 출력
print(s1)
print(s2)
print(s3)
print(s4)

print('### 여러 변수에 여러 값 대입 ###')
# 여러 변수에 여러 값을 한번에 대입할 수 있다.
a,b,c = 1,2,3
print(a,b,c)
# 한번에 대입할 경우와 순차적으로 대입할 때는 결과값이 다르다
a = 1
b = 5
a = b + 5
b = a + 9 
print(a,b)
a = 1
b = 5
a, b = b + 5, a + 9
print(a,b)

print('### 뮤터블, 이뮤터블 메모리 주소의 변화 ###')
# 뮤터블 자료형 : 리스트, 딕셔너리 ,집합 등이 있으면 값을 변경할 수 있다.
# 이뮤터블 자료형 : 수, 문자열, 튜플 등이 있으면 값 변경이 불가능하다.

# 리스트(뮤터블)같은 경우 리스트안에 원소를 추가,삭제,수정을 하여도 식별 번호(메모리주소)가 변경되지 않는다
a = [1,2,3]
print(a , id(a))
a.insert(0,2)
print(a , id(a))

# 정수(이뮤터블)같은 경우 해당 메모리 주소의 값이 변경되는 것이 아니라 새로운 값의 메모리 주소로 변경되는 것 이다.
num = 1
print(num , id(num))
num = 2
print(num , id(num))

print('### len()으로 리스트, 튜플의 길이 구하기 ###')
a = [1,2,3]
b = (1,2,3)
print(len(a), len(b))

print('### min(), max()로 배열의 최대,최소값 구하기 ###')
a = [1,55,77]
b = (2, 44, 66)
print(min(a), max(a), min(b), max(b))

print('### 비교 연산자로 배열의 대소 또는 등가 관계 판단하기 ###')
# - 비교연산자는 == 이다.
# - 맨 앞 원소부터 차례로 비교한다.
# - 원소수가 많은 배열을 큰 것으로 판단한다
# - 두 객체의 식별 번호가 같은지 비교할려면 is를 사용하자
# - 파이썬은 값을 비교할 때 등가성(==) 비교와 동일성(is) 비교를 사용하며 등가성 비교는 좌변과 우변의 값이 같은지만 비교하고 동일성 비교는 값은 물론 식별번호까지 같은지 비교한다
a = [1,2,3]
b = [1,2,4]
c = [1,2,3,4]
d = [1,2,3,5]
e = [1,2,3,4,5]
print(a == [1,2,3])
print(a == b)
print(a < b)
print(a == c)
print(a < c)
print(a < c < e)
print(a[0] is 1)
print(a is [1,2,3])

print('### 내포 표기 생성 ###')
a = [1,2,3]
b = [num * 2 for num in a if num % 2 == 1]
print(b)

    












