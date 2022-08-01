# https://www.acmicpc.net/problem/2908

A, B = input().split()

int_A = int(A[::-1])    # 상수가 거꾸로 읽은 수들을 비교해야하므로
int_B = int(B[::-1])    # int 형 변환

if int_A > int_B:
    print(int_A)
else:
    print(int_B)