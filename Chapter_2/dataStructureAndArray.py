'''
    파이썬의 배열은 리스트와 튜플로 구현할 수 있다.
    리스트와 튜플은 데이터 컨테이너라고 하며 원소를 변경할 수 있는지 없는지에 따라 차이가 있다.
'''

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

