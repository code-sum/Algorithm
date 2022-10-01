import sys
sys.stdin = open("1933_input.txt", "r")

# 정수 n을 반복문의 정수 i로 나누었을 때 나머지가 0이면
# i는 n의 약수라는 의미, i를 오름차순으로 출력
n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end = " ")