# https://www.acmicpc.net/problem/1543

import sys

input_ = sys.stdin.readline().strip()
word = sys.stdin.readline().strip()

len_word = len(word)
index_, cnt = 0, 0

while True:
    index_ = input_.find(word, index_)
    if index_ == -1:
        break
    cnt += 1
    index_ += len_word

print(cnt)



