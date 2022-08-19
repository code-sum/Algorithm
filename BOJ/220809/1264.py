# https://www.acmicpc.net/problem/1264

import sys
sys.stdin = open("1264.txt")

# 입력은 여러 개의 테스트 케이스로 이루어져 있으며, 
# 각 줄마다 영어 대소문자, ',', '.', '!', '?', 공백으로 이루어진 문장

while True:
    text = input()
    if text == '#':
        break

    cnt = 0
    for i in text:
        if i in 'AEIOUaeiou':
            cnt += 1
    print(cnt)