# 11856 반반

import sys

sys.stdin = open("_반반.txt")


# 첫 번째 줄에 테스트 케이스의 수 TC가 주어진다. 
# 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다.
T = int(input())

for tc in range(1, T+1):
    s = list(map(str, input()))

    # S에 정확히 두 개의 서로 다른 문자가 등장하고, 
    # 각 문자가 정확히 두 번 등장하는 지 판별
    # 이중 for문 작성해서 s[i]와 s[j] 비교
    result = 0
    for i in range(4):

        # 2개의 인덱스에 동일한 알파벳 들어갔으면 cnt += 1
        cnt = 0
        for j in range(4):
            if s[i] == s[j]:
                cnt += 1
        # s[i] == s[i] 인 경우까지 포함해서, 동일 알파벳 들어간 인덱스 발견하면(cnt == 2)
        # result += 1
        if cnt == 2:
            result += 1

    # 2가지 서로 다른 문자가 각각 2번씩 반복될 때, 
    # 예컨대 s[0] == s[1] and s[2] == s[3] 인 경우 result == 4
    if result == 4:
        print('#{} Yes'.format(tc))
    else:
        print('#{} No'.format(tc))