# https://softeer.ai/practice/info.do?idx=1&eid=1016

import sys

a, b = map(int, input().split())

if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("same")