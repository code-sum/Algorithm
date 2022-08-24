# https://www.acmicpc.net/problem/2511

import sys
sys.stdin = open("2511.txt")

# 승자는 각 라운드당 +3 승점
# 패자에게는 승점 없음
# 비길 경우 두 사람에게 +1 승점
# 라운드 종료 후 총점이 큰 사람이 승자
# 승점이 같으면 마지막에 이긴 사람이 승자

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_cnt = 0; b_cnt = 0
record = [0 for i in range(10)]

for i in range(10):
    if a[i] > b[i]:
        a_cnt += 3; record[i] = "A"
    elif a[i] < b[i]:
        b_cnt += 3; record[i] = "B"
    else:
        a_cnt += 1; b_cnt += 1; record[i] = "D"

# A점수가 더 높을 경우 출력
if a_cnt > b_cnt:
    print(a_cnt, b_cnt)
    print("A")

# B점수가 더 높을 경우 출력
if a_cnt < b_cnt:
    print(a_cnt, b_cnt)
    print("B")

# A와 B 총점이 동점일 경우 출력
if a_cnt == b_cnt:
    if a == b:
        print(a_cnt, b_cnt)
        print("D")
    else:
        print(a_cnt, b_cnt)
        for i in reversed(range(10)):
            if record[i] == "A":
                print("A"); break
            elif record[i] == "B":
                print("B"); break