time1 = input().split()
time2 = input().split()  
# time1, time2 는 리스트!

new_hour = int(time1[0]) + int(time2[0])
new_min = int(time1[1]) + int(time2[1])

print('{} {}'.format(new_hour, new_min))


# 모범 답안
import sys
sys.stdin = open("1976_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    hour, minute, next_hour, next_minute = map(int, input().split())
    result_hour = hour + next_hour
    result_minute = minute + next_minute

    if result_minute > 59 :
        result_hour += 1
        result_minute -= 60

    if result_hour > 12 :
        result_hour -= 12

    print('#%d %d %d' % (test_case, result_hour, result_minute))