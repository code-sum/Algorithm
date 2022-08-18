# https://www.acmicpc.net/problem/17388

# s, k, h 순서대로 입력
univ = list(map(int, input().split()))

if sum(univ)>=100:
    print("OK")
else:
    if min(univ) == univ[0]:
        print("Soongsil")
    elif min(univ) == univ[1]:
        print("Korea")
    else:
        print("Hanyang")