# https://www.acmicpc.net/problem/2979

# A: 1대 주차할 때 1대당 1분 요금
# B: 2대 주차할 때 1대당 1분 요금
# C: 3대 주차할 때 1대당 1분 요금

import sys
sys.stdin = open("2979.txt")

if __name__ == "__main__":

# 첫째 줄에 주차 요금 A, B, C
    A, B, C = map(int, input().split())
    time_range = [list(map(int, input().split())) for _ in range(3)]
    end = max(time_range[0][1], time_range[1][1], time_range[2][1])
    array = [0]*(end-1)

    for i in time_range:
        for j in range(i[0]-1, i[1]-1):
            array[j] += 1

    sum = 0
    for num in array:
        if num == 1:
            sum +=  A
        elif num == 2:
            sum += 2*B
        elif num == 3:
            sum += 3*C

    print(sum)