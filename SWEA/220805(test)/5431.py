T = int(input())
for test_case in range(1, T + 1):

    # 각 테스트 케이스의 첫 번째 줄에는 수강생의 수를 나타내는 정수 N(2≤N≤100)과 
    # 과제를 제출한 사람의 수를 나타내는 정수 K(1≤K≤N)가 공백으로 구분되어 주어진다.
    N, K = map(int, input().split())

    # 두 번째 줄에는 과제를 제출한 사람의 번호 K개가 공백으로 구분되어 주어진다.     
    submit = list(map(int, input().split()))

    # 전체 수강생 순회하면서 과제 안 낸 사람들의 번호 탐색
    result = []
    for i in range(1, N+1):
        if i not in submit:
            result.append(i)

    # 각 테스트 케이스마다 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력한다.
    # result 는 리스트니까, 그 안에 있던 요소들을 풀어서 출력하려면 (*)
    print(f'#{test_case}', *result)