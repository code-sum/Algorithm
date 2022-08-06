for _ in range(10):
    test_case = int(input())

    #  8개의 데이터가 주어진다.
    PW = list(map(int, input().split()))

    # 주어진 PW 리스트에서 0이 등장하기 전까지 반복문 연산 수행
    cnt = 1
    while 0 not in PW:

        # [사이클1] PW의 각 요소를 순회하며 1, 2, 3, 4, 5씩 감소시키기
        for i in range(len(PW)):
            PW[i] -= cnt
            cnt += 1

            # 감소시킬 값 cnt가 5보다 커져버리면 cnt = 1 로 초기화
            if cnt > 5:
                cnt = 1

            # PW의 각 요소가 음수가 되는 순간이 오면 0 값에 매핑
            if PW[i] <= 0:
                PW[i] = 0
                break

    # 0 값이 제일 마지막에 위치하도록 조정
    while PW[-1] != 0:
        PW.insert(0, PW.pop())

    print(f'#{test_case}', *PW)