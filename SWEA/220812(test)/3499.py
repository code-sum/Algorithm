# 3499 퍼펙트 셔플

import sys

sys.stdin = open("_퍼펙트셔플.txt")


# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
T = int(input())

for tc in range(1, T + 1):

    # 각 테스트 케이스의 첫 번째 줄에는 자연수 n
    n = int(input())

    # 두 번째 줄에는 N개의 카드가 공백으로 구분되어 주어진다.
    # 인덱스를 이용해야하므로 list 로 받기
    cards = list(input().split())

    # n이 짝수면 일단 카드 덱을 정확히 절반으로 나누기
    if len(cards) % 2 == 0:
        first_deck = cards[:len(cards)//2]
        second_deck = cards[len(cards)//2:]

    # n이 홀수면 교대로 놓을 때 먼저 놓는 쪽에 한 장이 더 들어가게
    else:
        first_deck = cards[:len(cards)//2 + 1]
        second_deck = cards[len(cards)//2 + 1:]

    # 반씩 나눈 카드 덱이 모두 빌 때까지 반복:
    ans = []
    while first_deck or second_deck:
        # first_deck 이나 second_deck 에 요소가 존재하면
        # 맨 첫 번째 요소를 떼서 ans 에 저장
        if first_deck:
            ans.append(first_deck.pop(0))
        if second_deck:
            ans.append(second_deck.pop(0))

    print(f'#{tc}', *ans)