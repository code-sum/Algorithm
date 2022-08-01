# https://www.acmicpc.net/problem/2577

A = int(input())
B = int(input())
C = int(input())

result = A*B*C
count = [0]*10    # 0부터 9까지 숫자의 등장 횟수를 의미하는 리스트

while True:
    count[result % 10] += 1   # A*B*C의 1의 자리 확인, 이걸 리스트의 인덱스로 1씩 증가
    result //= 10             # 1의 자릿수 다시 확인
    if result == 0:           # result == 0 일때 반복문 종료
        break

for i in range(10):
    print(count[i])            # count[] 가 가진 인덱스 값 출력