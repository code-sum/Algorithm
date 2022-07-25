import sys
sys.stdin = open("10953_input.txt", "r")

test_case = int(input())    # 맨 첫줄에 테스트 케이스 개수(5)가 주어진다
for _ in range(test_case):  # 5이전까지, 0, 1, 2, 3, 4번째 연산에 대하여
    a, b = map(int, input().split(','))  # 콤마(,)로 구분된 두 정수를 입력
    print( a+b )