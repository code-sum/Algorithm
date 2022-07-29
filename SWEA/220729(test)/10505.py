# 소득 불균형

# 테스트 케이스의 수를 입력
n = int(input())

# 테스트 케이스 번호는 #1 부터 시작되므로 range(1, n+1)
for _ in range(1, n+1):

    # n번째 연산의 사람 수 members
    members = int(input())

    # n번째 연산의 사람들이 벌고 있는 incomes
    incomes = list(map(int, input().split()))

    # 총 소득을 사람수로 나누어 평균 소득 구하기
    sum_incomes = sum(incomes)
    avg_incomes = sum_incomes / members

    # 집단의 평균 소득과 같거나 그보다 적은 소득이 있으면
    # count 변수를 1씩 증가시키기
    count = 0
    for i in incomes:
        if i <= avg_incomes:
            count += 1

    # 테스트 케이스의 번호, 구하려는 값을 차례로 출력
    print('#%d %d' % (_, count))
