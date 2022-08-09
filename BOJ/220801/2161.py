# 덱 활용하기
from collections import deque

# 첫째 줄에 정수 N(1 ≤ N ≤ 1,000)이 주어진다.
N = int(input())
card = deque(list(range(1, N+1)))

# 버린 카드를 담아줄 빈 리스트 생성
out = []

while card:
    # card 의 첫번째 요소를 popleft하여 out 에 담기 ------ (1) 떼서 버리기
    card_pop = card.popleft()
    out.append(card_pop)

    # card 의 두번째 요소를 card 의 맨 뒤에 append 하기 -- (2) 떼서 뒤에 붙이기
    if card:
        card_pop = card.popleft()
        card.append(card_pop)

# 첫째 줄에 버리는 카드들을 순서대로 출력한다. 
# 제일 마지막에는 남게 되는 카드의 번호를 출력한다.
# 덱으로 묶여있던 out 객체를 * 표기로 풀어서 print
print(*out)