# https://www.acmicpc.net/problem/11286

# 절대값 내장함수 abs() 쓰는 풀이법도 공부해보기!

import sys
sys.stdin = open("11286.txt")

import heapq

# 프로그램은 처음 비어있는 배열에서 시작하게 된다
heap = []

# 첫째줄에 연산의 개수 n이 주어진다
n = int(sys.stdin.readline())

# 다음 n개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다
for i in range(n):
    inputs = int(sys.stdin.readline())

    # inputs 내의 정수 x == 0 일때, 
    # 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거
    # 만약 배열이 비어있는데 가장 작은 값을 출력하라고 하면
    # 0 을 출력하면 됨
    if inputs == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])

    else:

        # 정수 x 가 양수이면, heap 에 x 부호 그대로 push
        if inputs > 0:
            heapq.heappush(heap, (inputs, inputs))
        
        # 정수 x 가 음수이면, heap 에 x 부호 바꾸어서 push 
        else:
            heapq.heappush(heap, (-inputs, inputs))