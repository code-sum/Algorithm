# https://www.acmicpc.net/problem/2292

'''
1단 : 1 / +1개 – 1로부터의 이동거리(result) 1
2단 : 2~7 / +6개 – 1로부터의 이동거리(result) 2
3단 : 8~19 / +12개 – 1로부터의 이동거리(result) 3
4단 : 20~37 / +18개 – 1로부터의 이동거리(result) 4
...
'''

n = int(input())

# 입력된 x가 몇단에 속하는지 출력하는 함수 test 작성
def test(x):

    # N단에 속한 숫자들의 갯수 = 1 + (6*1) + (6*2) + (6*3) + ... + {6*(N-1)}
    #                        = 6*{0 + 1 + 2 + 3 + ... + (N-1)}
    #                        = 6*{(N-1)*N/2}

    N = 1
    while True:

        # N단에 속한 숫자 중에 가장 큰 수 
        max_in_floor = 6*((N-1)*N/2) + 1

        # N단에 속한 숫자 중에 가장 작은 수
        if N == 1:
            min_in_floor = N
        else:
            min_in_floor = 6*((N-2)*(N-1)/2) + 2

        # if x 가 N단에 있을 때: return N
        if min_in_floor <= x <= max_in_floor:
            return N
        else:        
            N += 1

print(test(n))