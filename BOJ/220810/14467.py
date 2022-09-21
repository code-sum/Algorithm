# https://www.acmicpc.net/problem/14467

# 같은 번호의 소가 위치를 바꾼 것이 몇 번인지 센다
# 소가 길을 건너간 최소 횟수를 출력

import sys
sys.stdin = open("14467.txt")

t = int(input())
dic = {}
cnt = 0

for _ in range(1, t+1):
    # a 는 움직인 소의 번호
    # b 는 왼쪽(0)으로 갔는지, 오른쪽(1)으로 갔는지
    a, b = map(int, input().split())

    # 새로 나타난 소라면 딕셔너리에 키,값 쌍으로 번호,발견위치 추가
    if a not in dic:
        dic[a] = b
    # dic 에 넣은 소가 또 나타났는데
    else:
        # 그 소가 이전과 달리 위치를 바꿨으면
        if dic[a] != b:
            cnt += 1
            dic[a] = b

print(cnt)
