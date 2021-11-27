"""
    배열의 최댓값을 구할 때 max() 메소드를 사용안하고 구한다면 for문을 돌려서 if문으로 원소 하나###하나 비교하여 구하게 되는데
    이것을 알고리즘 용어로 '스캔' 이라고 한다.

"""
from typing import Any, Sequence
from testModule.arrayTestModule import min_of # 디렉토리에 접근할 때 / 가 아닌 .로 접근한다.
# Sequence는 시퀀스형을 의미하며 리스트, 바이트 배열, 문자열 튜플, 바이트열 등이 있다.
# Any는 아무 or 모든 자료형을 의미 

print('### 입력받은 정수의 최댓값 구하기 ###')

# 이 함수의 의미는 매개변수로 Sequence형을 받지만 함수안의 매개변수에 대한 함수 어노테이션(def test(a:annotation))은 시퀀스형이 아닌 뮤터블 시퀀스라고 명시한다. 
# 반환값은 Any라는 의미이다.
def max_of(a: Sequence) -> Any :  
    max_num = a[0]
    for i in range(1, len(a)):
        if a[i] > max_num:
            max_num = a[i]
    return max_num
 
# if 안의 __name__ 은 모듈객체이다. 모듈 객체에는 __name__, __loader__, __package__, __path__ 등등이 있다.
# 스크립트를 직접 실행할 때 변수 __name__은 '__main__' 이고 임포트될 때 변수 __name__은 원래의 모듈 이름이다. 음.. __name__을 사용하는 용도는 해당 파일을 직접 실행시키냐 아니냐 구분직기 위해 쓰는것으로 보인다.
if __name__=='__main__':
    print('__name__:::', __name__)
    print('배열의 최대/최소값을 구합니다.')
    num = int(input('원소 수를 입력하세요 : '))
    x = [None] * num 
    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요 :'))

    print(f'최댓값은 {max_of(x)} 입니다')
    print(f'최솟값은 {min_of(x)} 입니다')

# random.randint(lo,hi) lo 이상 hi 이하인 정수 난수 반환
import random
print('###난수의 최댓값 구하기###')
array_num = int(input('난수의 개수 입력 : '))
lo = int(input('난수의 최솟값 입력 : '))
hi = int(input('난수의 최댓값 입력 : '))
array = [None]*array_num
for i in range(array_num) : 
    array[i] = random.randint(lo,hi)       
    
print(f'{(array)}')
print(f'이 배열의 최댓값은 {max_of(array)} 입니다')

### 튜플, 문자열, 문자열 리스튼최댓값 구하기 ###
# 문자열같은 경우 최댓값을 구할 때 문자 코드가 높은 문자를 출력한다
print('### 튜플, 문자열, 문자열 리스튼최댓값 구하기 ###')

tuple = (1,2,3,4,5)
string = 'StRing'
array = ['ASD','ZXc','QWE']

print(f'{tuple}의 최댓값은 {max_of(tuple)}')
print(f'{string}의 최댓값은 {max_of(string)}')
print(f'{array}의 최댓값은 {max_of(array)}')

### 원소가 같은 리스트와 튜플 등가성(==) 동일성(is) 비교하기 ###
# - 리스트와 튜플은 서로 다른 식별번호를 가지기 때문에 동일성에는 False가 나온다
# - 하지만 대입을 하게되면 서로 같은 메모리 주소를 보기 때문에 True가 나온다
print('### 원소가 같은 리스트와 튜플 등가성(==) 동일성(is) 비교하기 ###')
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]
tuple1 = (1,2,3,4,5)
tuple2 = (1,2,3,4,5)

print('list1 == list2', list1 == list2) 
print('list1 is list2', list1 is list2) 
print('tuple1 == tuple2', tuple1 == tuple2) 
print('tuple1 is tuple2', tuple1 is tuple2) # 이상하다.. False가 나와야하고 cli로 실행 시 False가 나오는데 왜 동일한 식별번호를 갖지..??
print('list1 == tuple1', list1 == tuple1) 
print('list1 is tuple1', list1 is tuple1) 
list1 = list2
print('list1 == list2', list1 == list2) 
print('list1 is list2', list1 is list2)

### 리스트 스캔 ###
# - 리스트를 스캔하는 방법은 총 4가지가 있다(튜플도 똑같다)
# - 1. 리스트의 길이(len())를 알아내어 리스트의 길이 -1까지 반복하는 방법
# - 2. 인덱스와 원소를 짝지어 enumerate() 함수로 반복하는 방법
# - 3. 1부터 카운트 하는 방법
# - 4. 인덱스값을 사용하지 않고 in을 사용해서 원소를 처음부터 순서대로 꺼내는 방법

print('### 리스트 스캔 ###')
print('# 방법 1 #')
list1 = ['A','B','C','D']
for i in range(len(list1)) : 
    print(f'list1[{i}] = {list1[i]}')

print('# 방법 2 #')
for i, name in enumerate(list1) :
    print(f'list1[{i}] = {name}')

print('# 방법 3 #')
for i, name in enumerate(list1, i) :
    print(f'list1[{i}] = {name}')

print('# 방법 4 #')
for i in list1 : 
    print(i)

### 이터러블 ### 
# - 이터러블은 문자열, 리스트, 튜플, 집합, 딕셔너리 등의 자료형 객체를 반복 가능하다는 공통점을 가지고 있으며 원소를 하나씩 꺼내는 구조이다. 
# - 이터러블 객체의 내장 함수인 iter()의 인수로 전달하면 그 객체에 대한 이터레이터(반복자)를 반환한다.
# - __next__ 함수를 호출하거나 next() 함수에 이터레이터를 전달하면 원소를 순차적으로 꺼낼 수 있다.
# - 꺼낼 원소가 없는 경우에는 StopIteration으로 예외 발생을 시킨다.

print('### 배열 원소 역순 정렬하기 ###')
print('# 방법1. for문 돌리기 ')
"""
list1 = [1,2,3,4,5]
copy_list = [None] * int(len(list1)) 
for i in range(len(list1)) :
    length = len(list1) -1 -i
    print(list1[length], length)
    copy_list[i] = list1[length]

print(copy_list)
"""

from typing import Any, MutableSequence

def reverse_array(array:MutableSequence) -> None : 
    print('배열 원소를 역순으로 정렬 중')
    length = len(array)
    for i in range(length // 2) : # length가 홀수일 때는 가운데 원소를 제외하여 양쪽 을 대입하고 짝수일 경우 모두 대입한다
        array[i], array[length-i-1] = array[length - i - 1], array[i]

if __name__ == '__main__' : 
    print('배열의 원소를 역순으로 정렬')
    array_length = int(input('배열의 크기를 입력 : '))
    array = [None]*array_length

    for i in range(array_length)  :
        array[i] = int(input(f'array[{i}]값을 입력 : '))
    reverse_array(array)

    print('배열 원소를 역순으로 정렬 완료')
    for i in range(array_length) :
        print(f'array[{i}] == {array[i]}')

print('# 방법2. reverse() 사용하기 ')
# - 참고로 튜플은 이뮤터블하므로 역순으로 정렬 불가능하다
list1 = [1,2,3]
list1.reverse()
print(list1)

print('# 방법2-1. reversed() 사용하기 ')
# - 역순으로 정렬한 리스트를 다른 변수에 대입할려면 
list2 = [1,2,3]
reverse_list = list(reversed(list2))
print(reverse_list)

### 기수와 서수 ###
# - 기수란 수를 나타내는데 기초가 되는 정수를 말한다
# - 서수란 사물의 순서를 나타내는 것을 말한다
# - 예를 들면 1,2,3이 있다면 1,2,3은 기수를 얘기하는 것이고 첫 번째(1), 두 번째(2), 세 번째(3)를 서수라고 얘기한다

### 10진수 ###
# - 10종류의 수로 나타낸다(10~99까지) -> 0 1 2 3 4 5 6 7 8 9
# - 1234을 10진수로 표현하면 -> 1*10^3 + 2*10^2 + 3*10^1 + 4*10^0 = 1234으로 표현할 수 있다.(x*0은 1 이다)

### 8진수 ###
# - 8종류의 수로 나타낸다(10~77까지) -> 0 1 2 3 4 5 6 7
# - 8진수의 5306을 10진수로 표현하면 -> 5*8^3 + 3*8^2 + 0*8^1 + 6*8^0 = 2758 이고 2758를 다시 8진수로 나타내면 5306 이다

### 16진수 ###
# - 16종류의 수로 나타낸다(0~F는 10진수로 0~15를 의미한다) -> 0 1 2 3 4 5 6 7 8 9 A B C D E F (즉 9 부터는 10을 A 11을 B로 정의하면 된다)
# 12A0을 10진수로 표현하면 1*16^3 + 2*16^2 + 10*16^1 + 0*16*0 = 4,768 이다

### 36진수 ###
# - 36종류의 수로 나타낸다(0~Z는 10진수로 0~35를 의미한다) -> 0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
# 계산법은 위의 개념과 동일하다
print('### 10진수 정숫값을 입력받아 2~36진수로 변환하기')
def card_conv(x:int, r:int) -> str : 
    d = ''                                         # 문자열 변수 선언 
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 36진수로 표현해줄 문자열
    n =len(str(x))
    print(f'{r:2} | {x:{n}}')
    while x > 0 :               
        print('   +' + '-'*(n + 2))
        if x // r : 
            print(f'{r:2} | {x // r:{n}} --- {x % r}')
        else :
            print(f'     {x // r:{n}} --- {x % r}')
        d += dchar[x % r]                          # 정수(x)와 진수(r)를 나눈 나머지로 dchar에 해당하는 문자열을 뽑아낸다
        x //= r                                    # 정수(x)와 진수(r)를 나눈 몫으로 0이 될 때까지 실행한다
    return d[::-1] #역순으로 반한한다


if __name__ == '__main__' : 
    print('10진수를 n진수로 변환')
    
    while True  :
        while True : 
            no = int(input('변환할 값으로 음이 아닌 정수를 입력 : '))
            if no > 0 : 
                break
        while True : 
            cd = int(input('변환할 진수 입력 : '))
            if 2 <= cd <= 36 : 
                break
        print(f'{cd}진수로는 {card_conv(no, cd)}입니다')
        
        retry = input('계속 진행하시겠습니까?(Y/N) : ')
        if retry in {'N','n'} :
        # if retry == 'N' or retry == 'n'와 동일한 로직이다 
            break

"""
보통 다른 언어에서는 매개변수 값을 받을 때 call by value 또는 call by reference를 사용하지만
파이썬의 경우 이 2가지의 중간인 call by object reference라는 것을 사용한다
call by object reference는 이뮤터블일 경우와 뮤터블일 경우로 나뉜다

call by value(값에 의한 호출)       - 받은 인자의 값을 복사하여 처리
                                   - 장점 : 복사하여 처리하기 때문에 안전, 원래의 값 보존
                                   - 단점 : 메모리 주소 하나 더 생성하여 복사를 하기 때문에 메모리 사용량이 늘어난다 

call by reference(참조에 의한 호출) - 받은 인자의 주소를 참조하여 처리
                                   - 장점 : 복사하지 않고 직접 참조하기 때문에 빠름
                                   - 단점 : 직접 참조하기 때문에 원래 값에 영향을 미친다

call by object reference(객체 참조에 의한 전달)
                                   - 이뮤터블일 경우 : 매개변수로 받은 값의 타입이 이뮤터블일 경우 함수안에서 값이 변경된다 하더라도 원래의 값은 변하지 않는다  
                                   - 뮤터블일 경우 : 매개변수로 받은 값의 타입이 뮤터블일 경우 함수안에서 값을 변경하게 되면 변경된다  
                                   - 왜 이럴까 : 파이썬은 다른 언어와 달리 변수는 value의 메모리 주소를 참조하기 때문이다. 
"""

### 객체 참조에 의한 전달에 대한 예를 보자
# - 이뮤터블인 경우(수, 문자열, 튜플)
# - 기존 변수의 값은 유지되는 것을 볼 수 있다(변경된 값은 아예 다른 메모리 주소를 참조하기 때문이다)
int = 10
string = 'test'
tuple = (1,2,3)

def translateImmutable(int, string, tuple) : 
    int = 20
    string = 'test2222'
    tuple  = (4,5,6)
    return int, string, tuple

res_int, res_string, res_tuple = translateImmutable(int, string, tuple)
print(
    f"""
        ### 기존 value ###
        int ::: {int} intID ::: {id(int)}
        string ::: {string} stringID ::: {id(string)}
        tuple ::: {tuple}   tupleID ::: {id(tuple)}
        
        ### 변경 후 value ###
        res_int ::: {res_int} intID ::: {id(res_int)}
        res_string ::: {res_string} stringID ::: {id(res_string)}
        res_tuple ::: {res_tuple}   tupleID ::: {id(res_tuple)}
    """
)

# - 뮤터블인 경우(리스트, 딕셔너리, 집합)
# - 기존의 변수의 값이 변경되는 것을 볼 수 있다(뮤터블 같은 경우 해당 메모리 주소 안에 값이 변경되기 때문이다)

list = [1,2,3]
set = set({1,2,3})
dictionary = {'idx1': 1,'idx2': 2,'idx3': 3}

def translateMutable(list, set, dictionary) :
    list[0] = 4
    list[1] = 5
    list[2] = 6
    set.add('4')
    set.add('5')
    set.add('6')
    dictionary['idx1'] = 4
    dictionary['idx2'] = 5
    dictionary['idx3'] = 6


print(
    f"""
        ### 기존 value ###
        list ::: {list} intID ::: {id(list)}
        set ::: {set} stringID ::: {id(set)}
        dictionary ::: {dictionary}   dictionaryID ::: {id(dictionary)}
    """
)

translateMutable(list, set, dictionary)

print(
    f"""
        ### 변경 후 value ###
        list ::: {list} intID ::: {id(list)}
        set ::: {set} stringID ::: {id(set)}
        dictionary ::: {dictionary}   tupleID ::: {id(dictionary)}
    """
)

### 소수 나열하기 ###
"""
소수란? - 자신과 1 이외에 나누어 떨어지지 않는 정수 
       - 나누어 떨어지지 않는 정수로 수식어로 표현하면(1를 제외하고) : n-1
합성수란? - 나누어 떨어지는 정수가 하나 이상 존재하는 수

"""

import time
# 1000 이하의 소수 나열하기
# 이 소스를 보면 소수일 때 불필요하게 마지막까지 나눗셈을 실행한다
# 예를들면 7이 소수인지 보기위해 2,3,4,5,6 에서 4,6은 실행하지 않아도 된다. 이미지 2에서 나누어 떨어지면 4도 나누어 떨어질거고 3도 마찬가지다. 정리하자면 나누기 위한 숫자의 배수는 구지 나누지 않아도 된다는 것 이다. 
"""
start = time.time()
counter = 0
for i in range(2, 50001) :
    for j in range(2, i) : 
        counter += 1 
        if i % j == 0 : 
            break
    else :
        print(i)
print(f'나눗셈을 실행한 횟수 : {counter}')
print(f'실행 시간 : {time.time()-start}')   #17.178727865219116 
"""
# 1000 이하의 소수 나열하기(개선 1)
# 실행시간이 많이 개선된 것을 볼 수 있다. 참고로 빠른 알고리즘은 메모리 자원을 더 요구한다.
start = time.time()
counter = 0                             # 나눗셈 실행 횟수
ptr = 0                                 # 찾은 소수의 개수
prime = [None] * 50000                    # 찾은 소수를 저장하기 위한 배열

prime[ptr] = 2
ptr += 1

for i in range(3, 50001, 2) :            # 2는 이미 소수이기 때문에 3부터 2씩 늘려서 소수들만 확인 
    for j in range(1, ptr) :            # 찾은 소수 개수만큼만 실행
        counter += 1                    
        if i % prime[j] == 0 :
            break
    else :
        prime[ptr] = i
        ptr += 1

for i in range(ptr) : 
    print(prime[i])
print(f'나눗셈을 실행한 횟수 :  {counter}')
print(f'실행 시간 : {time.time()-start}')   # 2.0335805416107178

# 1000 이하의 소수 나열하기(개선 2)
# 정수 n은 제곱근 이하의 어떤 소수로도 나누어 떨어지지 않는다.
 
### 리스트의 원소와 복사 ###
# 파이썬에서 변수는 객체와 연결된 이름에 불과하며 리스트, 튜플의 원소 자료형을 미리 정할 필요가 없다(동적으로 자료형을 정한다).
x = [1,2,33.54,[22, 24], 'abc']
for i in range(len(x)):
    print(f'x[{i}]={x[i]} {type(x[i])}')

# 리스트의 얕은 복사 
# copy() 함수를 이용하여 얕은 복사를 할 수 있다.
# 얕은 복사를 하게 되면 복사를 한 변수는 다른 주소값을 참조한다.
# < 주의 >
# 하지만 리스트(뮤터블)안에 뮤터블한 자료형이 들어가 있는 상태에서 원소를 변경하게되면 같이 변경이 된다.
# 이유는 뮤터블 안에 뮤터블의 id를 찍어보면 copy한 변수의 뮤터블안의 뮤터블과 id()가 동일한 것을 알 수 있다.
x = [1,2,3]
y = x.copy()
x[0] = 4
print(f'{x}')
print(f'{y}')

x = [[1,2,3],[4,5,6]] # 뮤터블 안에 뮤터블이 속해 있는 경우
y = x.copy()
x[0][0] = 123
print(f'{x}')
print(f'{y}')
# 왜 이러는 걸까?? 함 id를 찍어보자
print(f'id(x) ::: {id(x)} , id(y) ::: {id(y)}') # copy한 변수와 id가 다르지만
print(f'id(x[0]) ::: {id(x[0])}, id(y[0]) ::: {id(y[0])})') # 뮤터블 안의 뮤터블의 id는 동일한 것을 알 수 있다.

# 리스트의 깊은 복사
# copy 모듈을 임포트 해줘야 하고 deepcopy() 함수를 이용하여 깊은 복사를 할 수 있다.
# 얕은 복사에서 원소 값이 같이 변경되는 상황을 피할려면 깊은 복사로 값만 복사를 해야한다.
# 하지만 그 만큼 메모리의 리소스를 차지하게 된다.
import copy
x = [[1,2,3,], [1,2,3]]
y = copy.deepcopy(x)
x[0][0] = 123
print(f'x ::: {x}')
print(f'y ::: {y}')















