# https://www.acmicpc.net/problem/11170

'''
3
0 10
33 1005
1 4
출력
2
199
0
'''

import sys
sys.stdin = open("11170.txt")

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    # N부터 M까지의 수를 str 으로 저장
    cnt = 0
    for i in range(N, M+1):
        word = str(i)
        # 0의 개수를 count
        cnt += word.count('0')

    # 각 테스트 케이스마다 N부터 M까지 0의 개수 출력
    print(cnt)
