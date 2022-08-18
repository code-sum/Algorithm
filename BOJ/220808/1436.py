# https://www.acmicpc.net/problem/1436

# 첫째 줄에 숫자 N이 주어진다
N = int(input())

# 종말의 숫자란 어떤 수에 6이 적어도 3개이상 연속으로 들어가는 수
# 666, 1666, 2666, 3666 ...
# 차례대로 진행할 때 N번째 종말의 숫자는?
# 666을 포함하는 수 가운데, 몇번째 숫자인가를 탐색하는 문제

cnt = 0
target_number = 666

while 1:
    if '666' in str(target_number):
        cnt +=1

    # 만약 '666'이 들어간 N번째 수를 찾으면:
    if cnt == N:
        print(target_number)
        break
    target_number += 1