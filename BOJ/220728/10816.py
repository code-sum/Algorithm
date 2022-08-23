# https://www.acmicpc.net/problem/10816

from sys import stdin
from collections import Counter

n = stdin.readline()
n_cards = stdin.readline().split()
m = stdin.readline()
m_cards = stdin.readline().split()

# 리스트 n_cards 을 Counter에 넣으면 
# N의 요소들의 숫자를 센 Dictionary자료형이 출력
C = Counter(n_cards)

# Counter(n_cards)에 M의 요소가 있다면 해당 숫자를 출력하고 없으면 0을 출력
print(' '.join(f'{C[m]}' if m in C else '0' for m in m_cards))