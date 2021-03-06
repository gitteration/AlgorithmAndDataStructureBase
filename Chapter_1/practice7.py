'''
### 변수 ###

파이썬에서는 데이터, 함수, 클래스, 모듈, 패키지 등을 모두 객체로 취급하며 변수는 값을 갖지 않는 특징이 있다.
- 변수는 객체를 참조하는 객체에 연결된 이름에 불과하다.
- 모든 객체는 메모리를 차지하고, 자료형뿐만 아니라 식별 번호를 가진다.
JS같은 경우에는 변수를 선언하면 변수명은 메모리 주소를 참조하고 해당 주소에 할당된 값을 가져오는거와는 다른거 같다.
정리하자면 값은 이미 해당 메모리 주소에 할당되어있고 해당 값으로 할당한 변수들은 해당 메모리 주소(값이 할당된)를 참조하게 되는 것 이다.



'''

# 식별 번호(메모리 주소) 출력하기
# 해당 값이랑 변수랑 메모리 주소가 같다
n = 17
id1 = int(id(17))
id2 = int(id(n))
print(f'id of {n} :::, {id1}, {n}')
print(f'id of n :::, {id2}, {n}')
print()

# 전역 변수와 지역 변수 메모리 주소 출력하기
# 전역변수에 선언한 변수의 메모리 주소와 지역변수에 선언한 변수의 메모리 주소는 같다
n = 1
def test() :
    x = 1 
    print(f'id(x) ::: {id(x)}')    
test()
print(f'id(1) ::: {id(1)}')
print(f'id(n) ::: {id(n)}')

# 그렇다면 값만 복사해서 다른 메모리 주소를 갖게해서 서로 다른 변수로 할려면??? copy를 이용하자
ori = [1,2,3]
copy = ori
print(f'{id(ori)}, {id(copy)}')
copy = ori.copy()
print(f'{id(ori)}, {id(copy)}')
