import sys
sys.stdin = open("2071_input.txt", "r")

n = int(input())
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    sum_value = sum(data)
    avg_value = sum_value // 10
    if sum_value % 10 >= 5:
        avg_value += 1
    
    print("#%d %d" % (i, avg_value))