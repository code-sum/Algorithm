# https://www.acmicpc.net/problem/2864

# 두 수의 가능한 합 중에서
# 최댓값과 최솟값을 구해 출력하자

# 5를 5로 보고 6을 5로 볼 때 (최소)
# 5를 5로 보고 6을 6으로 볼 때 (정상)
# 5를 6으로 보고 6을 5로 볼 때 (정상과 같음)
# 5를 6으로 보고 6을 6으로 볼 때 (최대)

a, b = input().split()

min = int(a.replace('6', '5')) + int(b.replace('6', '5'))
max = int(a.replace('5', '6')) + int(b.replace('5', '6'))

print(min, max)