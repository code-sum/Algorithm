import sys
sys.stdin = open("1989_input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    cycle = input()
    if cycle == cycle[::-1]:
        print('#{} {}'.format(test_case, 1))
    else:
        print('#{} {}'.format(test_case, 0))