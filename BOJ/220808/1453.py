# https://www.acmicpc.net/problem/1453

'''
3
1 2 3
출력 0
'''


# 첫째 줄에 손님의 수 N이 주어진다.
N = int(input())

# 둘째 줄에 손님이 들어오는 순서대로 각 손님이 앉고 싶어하는 자리 입력
location = list(map(int, input().split()))

# 1번부터 100번까지 PC방 자리
PC = [0] * 101

# 손님이 외친 자리에 사진이 없으면 그 손님은 자리 차지,
# 만약 선점한 사람이 있으면 거절 당함!  ->   거절당하는 수를 출력

cnt = 0 # 거절
for i in location:
    if PC[i] != 0:
        cnt += 1
    else:
        PC[i] += 1

print(cnt)