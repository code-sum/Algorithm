# 1208 Flatten

import sys

sys.stdin = open("_Flatten.txt")


# 총 10개의 테스트 케이스가 주어지며, 
# 각 테스트 케이스의 첫 번째 줄에는 덤프 횟수가 주어진다. 
# 그리고 다음 줄에 각 상자의 높이값이 주어진다.

for tc in range(1, 11):
    dump_cnt = int(input())
    box_list = list(map(int, input().split()))

    # 제한된 횟수만큼 옮기는 작업을 한 후 
    # 최고점과 최저점의 차이를 반환하는 프로그램을 작성
    for _ in range(dump_cnt):

        # 최고점이 있는 인덱스를 찾아서 max_index 에 저장
        max_index = box_list.index(max(box_list))
        # 최고점의 높이를 -1씩 깎기
        box_list[max_index] -= 1

        # 최저점이 있는 인덱스를 찾아서 min_index 에 저장
        min_index = box_list.index(min(box_list))
        # 최저점의 높이를 +1씩 증가
        box_list[min_index] += 1

    # for문 순회로 평탄화가 끝난 후 최고점과 최저점 높이의 차이 구하기
    ans = max(box_list) - min(box_list)

    print('#{} {}'.format(tc, ans))
