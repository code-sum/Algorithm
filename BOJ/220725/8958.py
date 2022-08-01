# https://www.acmicpc.net/problem/8958

# 첫째 줄에 테스트 케이스의 개수
test_case = int(input())

for _ in range(test_case):
    OX = input()
    score = 0
    count = 0
    for i in range(len(OX)):
        if OX[i] == "O":
            count += 1
            score += count
        if OX[i] == "X":
            count = 0
    print(score)