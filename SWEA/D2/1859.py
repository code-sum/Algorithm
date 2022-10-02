import sys

sys.stdin = open("1859.txt")

# 테스트 케이스 개수 t
t = int(input())

for i in range(1, t + 1):

    # 각 테스트 케이스마다 총 판매일 수 n, 일수별 매매가 input_
    n = int(input())
    input_ = list(map(int, input().split()))
    ans = 0
    max_price = 0  # max_price : 판매 시점에서 기준이 되는 가격

    for j in input_[::-1]:
        if j >= max_price:
            max_price = j
        else:
            ans += max_price - j

    print(f"#{i} {ans}")
