# 입력받은 점수의 부호(양수, 음수, 0) 출력하기
# if문의 else에 pass가 기본적으로 포함되어있어 빈 문장일 경우 pass가 실행됨 

def med(score):
    if(score > 0):
        return "양수"
    elif(score < 0):
        return "음수"
    else :
        return 0

print('점수의 부호(양수, 음수, 0) 출력하기 ')
score = int(input('score의 값 : '))
print(f'score의 점수는 {score} 이고 부호(양수, 음수, 0)은 {med(score)}이다.')


# 삼항 연산자 
x = int(1)
y = int(2)
a = int(x if x > y else y)
print(f'a는  {a} 입니다.')
