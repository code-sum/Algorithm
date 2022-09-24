import sys
sys.stdin = open("2027.txt")

for i in range(5):
    for j in range(5):
        if i == j:
            print("#", end='')
        else:
            print("+", end='')
    print()