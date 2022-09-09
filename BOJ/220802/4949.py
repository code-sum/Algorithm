# https://www.acmicpc.net/problem/4949

import sys
sys.stdin = open("4949.txt")

while True:
    in_ = input()

    # 반복문 종료조건
    if in_ == ".":
        break

    # 비어있는 스택, 스택 내용물 짝 맞는지 판별하는 불린형 변수 선언
    s = []
    bol = True

    for i in in_:
        if i == "(" or i == "[":
            s.append(i)
        elif i == ")":
            if not s or s[-1] == "[":
                bol = False
                break
            elif s[-1] == "(":
                s.pop() 
        elif i == "]":
            if not s or s[-1] == "(":
                bol = False
                break
            elif s[-1] == "[":
                s.pop()

    if bol == True and not s:
        print("yes")
    else:
        print("no")

    

