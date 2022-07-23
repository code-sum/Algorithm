import sys
sys.stdin = open("1938_input.txt", "r")

a, b = map(int, input().split())  # 두 자연수 a, b 가 빈칸을 두고 주어진다

print(a + b)
print(a - b)
print(a * b)
print(a // b)