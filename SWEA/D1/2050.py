import sys
sys.stdin = open("2050_input.txt", "r")

char = input()
# 출력하려는 값 = 0, 1, 2, 3, ... n-1
# ord(): 특정 문자의 아스키코드 값으로 변환
# A는 65에 해당하므로 64를 빼줌

for i in char:
    print(ord(i)-64, end = ' ')