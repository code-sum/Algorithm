# https://www.acmicpc.net/problem/4673

# for i in range(1, 10001):
#     생성자(i) = 
#     셀프넘버(i) = 생성자가 없는 수
#     print(셀프넘버)

def d(n):
    n = n + sum(map(int, str(n)))
    return n

not_self_num = set()
for i in range(1, 10001):
    not_self_num.add(d(i))

for j in range(1, 10001):
    if j not in not_self_num:
        print(j)