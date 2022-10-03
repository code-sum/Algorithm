# https://www.acmicpc.net/problem/2897

# 8월10일 코드리뷰

# 델타탐색 문제
# 0) [0] * 5 의 저장 리스트를 만들어서 0대, 1대, 2대 ... 부술 때마다 += 1
# 1) dy, dx 델타 배열을 먼저 만듬
#    주어진 문제에서 8방위 중에 어디를 탐색할지 생각해보면,
#    한 점을 기준으로, 우, 우하, 하 3방향을 탐색하면 됨
#    이때, 탐색 방향은 좌에서 우로, 위에서 아래로
#    나머지 방향은 탐색할 필요없음
#    우, 우하, 하 : x+1 ,(y+1,x+1), y+1
# 2) 문제에서 고려할 조건은 2가지
#    먼저, 빌딩(#)이 있으면 주차를 할 수 없다(=기준좌표가 될수없다)
#    그 다음, 기준좌표에 차(X)가 있으면 부순 차의 개수 +1 상태로 시작

import sys

sys.stdin = open("2897.txt")

dx = [0, 1, 1]
dy = [1, 1, 0]
BUILDING = "#"
CAR = "X"
VOID = "."

# 숫자가 공백으로 나뉘어져있는 입력
X, Y = list(map(int, input().split()))

list_ = []

# X 줄 만큼의 리스트를 입력
for _ in range(X):
    # 숫자 X 문자 O
    # 공백 X
    temp_list = list(input())
    list_.append(temp_list)

# 부순 횟수를 저장할 리스트
# 0개 1개 2개 3개 4개 부순횟수를 저장
break_count_list = [0] * 5

# 이중 반복문
for x in range(X):
    for y in range(Y):
        # 차를 부순 횟수는 탐색을 할 때마다 초기화(0)
        break_count = 0

        # 조건 1. 기준 좌표가 빌딩(#)이면 안된다.
        if list_[x][y] == BUILDING:
            # 이 다음 반복문의 코드들을 무시하고, 다음 값을 탐색
            continue

        # 성립이 안되는 조건들은 continue로 지나가고,
        # 조건이 성립될 때만 정상적인 코드를 실행한다.

        # 조건 2. 기준 좌표가 차라면 부순 횟수 + 1
        if list_[x][y] == CAR:
            break_count += 1

        """
        델타탐색을 하는 로직
        """
        for d in range(3):
            next_x = x + dx[d]
            next_y = y + dy[d]

            # 조건 1. 범위를 벗어나면 안된다.
            if not (-1 < next_x < X and -1 < next_y < Y):
                break

            # 조건 2. 탐색 좌표에 빌딩이 있으면 안된다.
            if list_[next_x][next_y] == BUILDING:
                break

            # 조건 3. 탐색 좌표에 차가 있으면 부순 횟수를 + 1
            if list_[next_x][next_y] == CAR:
                break_count += 1

        # break를 만나지 않고 for문이 끝났다면
        # 혜빈이가 정상적으로 주차를 했다는 소리
        else:
            break_count_list[break_count] += 1

# print(break_count_list)
# 정답 출력
for count in break_count_list:
    print(count)
