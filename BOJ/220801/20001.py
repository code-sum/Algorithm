# https://www.acmicpc.net/problem/20001

import sys
sys.stdin = open("20001.txt", "r", encoding="UTF-8")

list_ = []
 
while True:
    s = input()

    if s == '문제':
        list_.append(1)

    elif s == '고무오리':
        if not list_:
            list_.append(1)
            list_.append(1)
        else:
            list_.pop()
            
    elif s == '고무오리 디버깅 끝':
        break
 
if not list_:
    print('고무오리야 사랑해')
else:
    print('힝구')