#메인에서 함수를 부름->제너레이터가 숫자 생성-> 입력에서 숫자를 받음-> 입력받은 숫자를 로직 매개변수에 넘김->내가 그 숫자를 제너레이터에서 생성한
#답과 비교하여 출력형식 0S 0B를 반환함.
#비교방법: 4자리수 answer를 제너레이터가 만든 정답 변수와 비교 -> strike, ball 계산
#strike: 자리와 숫자가 완전히 일치 할때
#ball: 숫자는 맞지만 위치가 다를 때
#out 처리 -> 0S 0B
import pygame


#S검사후-> S를 제외한 문자를 B검사
def compare(answer, correct_answer):
    s = 0
    b = 0

    #S검사
    for i in range(len(answer)):
        if answer[i] == correct_answer[i]:
            s += 1
    #B검사
    for i in range(len(answer)):
        #1234 3421
        if answer[i] != correct_answer[i] and answer[i] in correct_answer:
            b += 1

    return f"{s}S {b}B"


print(compare("4321", "1234"))
