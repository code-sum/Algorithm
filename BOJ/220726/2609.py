import math     # 최대공약수, 최소공배수 출력하는 함수는 math 라이브러리 이용!

# 첫째 줄에 두 개의 자연수가 주어진다.
n, m = map(int, input().split())   # 두 수 사이에 한 칸의 공백이 주어진다.

print(math.gcd(n, m))   # 첫째 줄에는 두 수의 최대공약수 출력
print(math.lcm(n, m))   # 둘째 줄에는 두 수의 최소공배수 출력


######### 다른 코드 #########
# 시간 복잡도를 줄일 수 있음 #
#############################
a, b = map(int, input().split())

def GCD(a, b):
    while b:
        a, b = b, a % b
    return a
print(GCD(a, b))
def LCM(a, b):
    result = (a * b) // GCD(a, b)
    return result
print(LCM(a, b))