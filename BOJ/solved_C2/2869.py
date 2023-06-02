# https://www.acmicpc.net/problem/2869

a, b, v = map(int, input().split())

day_cnt = (v-b)/(a-b)

print(int(day_cnt) if day_cnt == int(day_cnt) else int(day_cnt)+1)