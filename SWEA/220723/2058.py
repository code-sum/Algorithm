import sys
sys.stdin = open("2058_input.txt", "r")

number = input()              # 하나의 자연수를 입력 받아
result = 0

for i in range(len(number)):  # 그 자연수(6789)의 길이(4)만큼 연산 진행
    result += int(number[i])  # i = 0, 1, 2, 3
print(result)                 # result = 0+6 -> (0+6)+7 -> (0+6+7)+8 -> (0+6+7+8)+9
