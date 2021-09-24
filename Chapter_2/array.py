"""
    배열의 최댓값을 구할 때 max() 메소드를 사용안하고 구한다면 for문을 돌려서 if문으로 원소 하나###하나 비교하여 구하게 되는데
    이것을 알고리즘 용어로 '스캔' 이라고 한다.

"""
from typing import Any, Sequence
from testModule.arrayTestModule import min_of
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

