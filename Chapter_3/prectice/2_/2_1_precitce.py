# while 문으로 작성한 선형 검색 알고리즘
from typing import Any, Sequence
'''
def seq_search(a: Sequence, keyWord : Any) -> int :
    i = 0
    while True :
        if i == len(a) :
            return -1
        if a[i] == keyWord :
            print({i})
            return i
        i += 1
'''
# while 문 대신 for문을 사용하면 간결해진다.
def seq_search(a: Sequence, keyWord : Any) -> int :
    i = 0
    for i in range(len(a)) :
        if a[i] == keyWord :
            return i    
    return -1        

if __name__=='__main__' :
    num = int(input('원소 수를 입력하세요. : '))
    x = [None]*num 
    
    for i in range(num) :
        x[i] = int(input(f'x[{i}] :'))

    keyWord = int(input('검색할 값을 입력하세요.: '))
    
    idx = seq_search(x, keyWord)
    if idx == -1 :
        print(f'검색한 값이 없습니다. ')
    else : 
        print(f'검색값은 x[{idx}]에 있습니다. ')