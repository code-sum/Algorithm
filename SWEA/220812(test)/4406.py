# 4406 모음이 보이지 않는 사람

import sys

sys.stdin = open("_모음이보이지않는사람.txt")


# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
T = int(input())

# 각 테스트 케이스의 첫 번째 줄에는 길이가 50이하이고 알파벳 소문자만으로 이루어진 
# 단어가 주어진다. 이 단어에 모음이 아닌 문자(자음)이 적어도 하나는 들어있다는 것이 보장된다.
for tc in range(1, T+1):
    word = input()

    # 모음이 삭제된 word를 담아줄 변수 ans
    ans = ''

    # word 에 모음이 포함되어 있으면 지나가기 continue
    # word 에 모음이 아닌 다른 알파벳 등장하면 ans 에 넣어주기
    for i in range(len(word)):
        if word[i] in ['a', 'e', 'i', 'o', 'u']:
            continue
        ans += word[i]

    print('#{} {}'.format(tc, ans))