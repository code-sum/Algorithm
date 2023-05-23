# https://www.acmicpc.net/problem/4153

while True:
    list_ = list(map(int, input().split()))

    # 중단조건
    if sum(list_) == 0:
        break

    else:

        list_2 = []
        for i in list_:
            list_2.append(i**2)

        # 내림차순 정렬    
        list_2 = sorted(list_2, reverse=True)

        # 가장 긴 변에 대한 정보를 max_length 에 저장
        max_length = list_2[0]

        # 가장 긴 변 list_2 에서 제거
        del list_2[0]

        if max_length == sum(list_2):
            print("right")
        else:
            print("wrong")

