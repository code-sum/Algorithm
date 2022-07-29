# 직사각형 길이 찾기

# 테스트 케이스의 수를 입력
n = int(input())

# 테스트 케이스 번호는 #1 부터 시작되므로 range(1, n+1)
for _ in range(1, n+1):

    # 테스트 케이스마다 직사각형 3변의 길이들을 입력 받음
    side_lens = list(map(int, input().split()))

    ans = 0

    # 만약 side_lens의 첫번째 요소와 같은 값이 3개 있다면
    # (= 3개의 변의 길이가 모두 같다면) 그 요소를 출력하게끔 ans 에 넣어줌
    if side_lens.count(side_lens[0]) == 3:
        ans = side_lens[0]
    else:

        # 만약 side_lens 요소 중에 제일 긴(max) 값이 1개만 있다면
        # (= 남은 2개의 길이가 이보다 짧다면) 그 요소를 출력하게끔 ans 에 넣어줌
        if side_lens.count(max(side_lens)) == 1:
            ans = max(side_lens)
        else:
            # 그 밖의 나머지 경우: 제일 긴 값이 2개인 경우
            # 제일 짧은(min) 값을 출력하게끔 ans 에 넣어줌
            ans = min(side_lens)

    print('#%d %d' % (_, ans))