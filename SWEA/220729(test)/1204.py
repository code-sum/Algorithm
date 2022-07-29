# 최빈수 구하기

# 테스트 케이스의 수를 입력
n = int(input())

for _ in range(n):
    test_case = int(input())

    # 1000명의 점수(scores)를 list에 담음
    scores = list(map(int, input().split()))

    # 1000명의 점수에 인덱스 순서를 주기 위해
    # 0이 1001개 있는 리스트를 만듬
    # 리스트 1번째 요소의 인덱스가 0이므로, 0을 1000개가 아닌 1001개 생성
    seq = [0] * 1001

    # 0, 0, 0, 0 으로 비어있는 seq 에,
    # scores 내 특정 점수들이 등장할 때마다 빈도 +1 씩 증가하도록
    # 반복문을 작성
    for i in scores:
        seq[i] += 1

    # seq 중에 가장 큰 값 = 1000개의 케이스 중에 가장 많이 등장한 점수
    find_max = max(seq)

    # find_max 중에서도 크기가 큰 값들 모아서 비교하기 위해
    # 새로운 리스트 컨테이너 ans 생성
    ans = []

    for i in range(len(seq)):
        if seq[i] == find_max:
            ans.append(i)

    # 테스트 케이스 번호와 최빈값 함께 print
    print('#%d %d' % (test_case, max(ans)))