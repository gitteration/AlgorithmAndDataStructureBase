
from typing import Any, Sequence


def min_of(a: Sequence) -> Any :
    print('다른 경로에 있는 파일 함수 실행')
    print('__name__:::' , __name__)
    min_num = a[0]
    for i in range(1, len(a)):
        if a[i] < min_num:
            min_num = a[i]
    return min_num