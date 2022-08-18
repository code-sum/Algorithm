# https://www.acmicpc.net/problem/2309

import sys
sys.stdin = open("2309.txt")

# 일곱명의 난쟁이 키 합계 = 100
# 아홉명 중에 이 합계를 만족하는 일곱명 선택하기

# conbinations 라이브러리를 이용한다!
import itertools

# 아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다.
heights = [int(input()) for _ in range(9)]

# 중복없이 7명을 선택
for i in itertools.combinations(heights, 7):

    # 만약 i 값들의 합계가 100이라면:
    if sum(i) == 100:

        # 선택했던 7명을 오름차순으로 정렬하여 출력
        for j in sorted(i):
            print(j)
        break