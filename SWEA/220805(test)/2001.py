T = int(input())
for test_case in range(1, T + 1):

    # 각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고
    N, M = map(int, input().split())

    # 다음 N 줄에 걸쳐 N x N 배열이 주어진다.
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    # 파리채 영역에 대한 순회 진행
    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):

            # 파리채 영역(MxM) 내부 인덱스를 탐색해 합계(sum) 구하기
            sum = 0
            for k in range(M):
                for l in range(M):
                    sum += matrix[i+k][j+l]

            # 더 큰 sum 이 등장할 때마다 result 갱신하기
            if sum > result:
                result = sum

    # 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
    print('#%d %d' % (test_case, result))