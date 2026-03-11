
import pygame
import pygame_gui
quiz_len = 4
def before_check(answer):
    #자릿수를 꽉안채운 경우나, 공백, 숫자가 아닌 경우도 false
    if not(len(answer) == quiz_len and answer.isdigit()): #isdigit함수는 공백, 문자 => 숫자가 아닌 모든 문자를 제외시킴
        print("answer is too short or too big or empty!")
        return False
    #단어 중복 검사. 4자리 숫자는 각각 다른 숫자여야함.
    for i in range(0, len(answer)):
        for j in range(i +1, len(answer)):
            if(answer[i] == answer[j]):
                print("dupicated number!")
                return False
                
    print("pass")
    return True



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





