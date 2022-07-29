# 신용카드 만들기1

n = int(input())

for _ in range(1, n+1):
    numbers = list(map(int, input().split()))

    # 리스트에서 홀수번째 요소만 뽑아냄
    hol = numbers[0::2]

    # 리스트에서 짝수번째 요소만 뽑아냄
    zzak = numbers[1::2]

    # 홀수번째 요소에 X2 씩해서 모두 더하기
    # (= 홀수번째 요소들의 합을 구한 다음, 그 값에 X2 하기)
    holX2_sum = (sum(hol))*2

    # 짝수번째 요소들을 모두 더하기
    zzak_sum = sum(zzak)

    # 16번째 숫자 N 정의하기
    for N in range(0, 10):
        if (holX2_sum + zzak_sum + N) % 10 == 0:
            print('#%d %d' % (_, N))