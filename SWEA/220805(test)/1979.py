T = int(input())
for test_case in range(1, T + 1):

    # 테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K
    N, K = map(int, input().split())

    # 퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0
    puzzle = []
    for _ in range(N):
        puzzle.append(list(map(int, input().split())))

    # 퍼즐을 행 탐색하면서 길이가 K인 단어가 들어갈 자리 있는지 찾기
    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N):

            # 1 값을 갖는 곳은 단어가 들어갈 수 있는 자리므로 cnt += 1
            if puzzle[i][j] == 1:
                cnt += 1

            # 0 값는 갖는 곳은 장애물 때문에 단어가 못 들어갈 자리
            # 혹은 j == N-1 로 N행 탐색중 맨 끝 열에 닿았을 경우
            # 추가적인 조건문을 작성하여 그 행의 result 값을 정산하도록 함
            if puzzle[i][j] == 0 or j == N-1:

                # cnt 센 값이 K랑 같으면 단어 넣을 공간이 하나씩 추가로 생긴거니까 result += 1 정산
                if cnt == K:
                    result += 1
                if puzzle[i][j] == 0:
                    cnt = 0

    # 퍼즐을 열 탐색하면서 길이가 K인 단어가 들어갈 자리 있는지 찾기
    # 구체적인 논리구조는 행 탐색때와 동일
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0 or j == N-1:
                if cnt == K:
                    result += 1
                if puzzle[j][i] == 0:
                    cnt = 0

    # 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력
    print('#%d %d' % (test_case, result))