# https://www.acmicpc.net/problem/5800

import sys
sys.stdin = open("5800.txt")

'''
2
5 30 25 76 23 78
6 25 50 70 99 70 90
'''

K = int(input())

for k in range(1, K+1):
    class_score = list(map(int, input().split()))

    # class_score 에서 점수만 따로 떼어내기
    scores = class_score[1:]
    scores_sorted = sorted(scores) # 내림차순 정렬

    # 인접한 두 수의 차이 중에 가장 큰 값 찾기
    gap = 0
    for i in range(0, len(scores_sorted)-1):
        if scores_sorted[i+1] - scores_sorted[i] > gap:
            gap = scores_sorted[i+1] - scores_sorted[i]
    
    # 두 줄로 출력
    print(f'Class {k}')
    print(f'Max {max(scores_sorted)}, Min {min(scores_sorted)}, Largest gap {gap}')