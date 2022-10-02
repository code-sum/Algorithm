import sys

sys.stdin = open("1204.txt")

t = int(input())

for i in range(1, t + 1):
    # 테스트 케이스 번호 n
    n = int(input())

    dic = {}
    input_ = list(map(int, input().split()))
    for j in input_:
        if j in dic:
            dic[j] += 1
        else:
            dic[j] = 1

    # 딕셔너리에서 가장 큰 value 를 갖는 key 를 찾을 때
    # max(dic, key=dic.get)
    print(f"#{n} {max(dic, key=dic.get)}")
