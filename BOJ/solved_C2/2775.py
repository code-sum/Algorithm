# https://www.acmicpc.net/problem/2775

t = int(input())

for _ in range(t):
    k = int(input())  # k층
    n = int(input())  # n호

    '''
    a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 
    사람들을 데려와 살아야 한다.
    단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

    k층 n호 : members명 거주
    0층 1호 : 1명 거주
    0층 2호 : 2명 거주
    0층 3호 : 3명 거주

    1층 1호 : 1명 거주
    1층 2호 : 1+2 = 3명 거주
    1층 3호 : 1+2+3 = 6명 거주

    2층 1호 : 1명 거주
    2층 2호 : 1 + (1+2) = 4명 거주
    2층 3호 : 1 + (1+2) + (1+2+3) = 10명 거주

    '''
    
    members = []
    for i in range(1, n+1):
        members.append(i)

    for i in range(k):
        for j in range(1, n):
            members[j] += members[j-1]

    # k층n호에 몇명이 살고있는지 members 출력
    print(members[-1])