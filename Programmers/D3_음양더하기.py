# https://school.programmers.co.kr/learn/courses/30/lessons/76501

# 음양더하기


def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] = -absolutes[i]
    return sum(absolutes)