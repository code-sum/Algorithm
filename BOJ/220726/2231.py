# https://www.acmicpc.net/problem/2231

# 첫째 줄에 자연수 N이 주어진다
N = int(input())
d_sum = 0          # 반복문 시작 전에 분해합 연산 초기화

for i in range(1, N+1):
    box = list(map(int, str(i)))   # N의 각 자릿수 숫자를 개별 요소로 갖는 리스트 생성(나중에 연산해야하므로 map ~ int 변환)
    d_sum = i + sum(box)           # N의 분해합
    if d_sum == N:        # N의 분해합 = d_sum 의 생성자일 때, 가장 작은 생성자 도출
        print(i)          # 이때의 생성자(i)를 출력!
        break             # 최소 생성자를 찾았으니 연산도 여기서 멈춤

    if i == N:        # 만약 생성자가 없는 경우 (분해합0 = 생성자0 + 각자리수0 의 구조! 즉, 분해합과 자연수N이 0으로 같을 때)
        print(0)      # 결과는 0을 출력