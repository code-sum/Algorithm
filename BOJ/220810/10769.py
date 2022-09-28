# https://www.acmicpc.net/problem/10769

import sys

sys.stdin = open("10769.txt")

input_ = input()
hap_cnt = 0
sad_cnt = 0

for i in range(0, len(input_) - 2):
    if input_[i] == ":" and input_[i + 1] == "-":
        if input_[i + 2] == ")":
            hap_cnt += 1
        elif input_[i + 2] == "(":
            sad_cnt += 1

if hap_cnt == 0 and sad_cnt == 0:
    print("none")
else:
    if hap_cnt > sad_cnt:
        print("happy")
    elif hap_cnt < sad_cnt:
        print("sad")
    else:
        print("unsure")
