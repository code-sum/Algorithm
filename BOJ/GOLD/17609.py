# https://www.acmicpc.net/problem/17609

import sys
sys.stdin = open("17609.txt")

'''
input_ 리스트가
회문(return 2), 유사회문(return 1), 
혹은 둘다 아닌지(return 0) ver 함수로 검증
'''

def ver(input_, cnt):
    rev_input_ = list(reversed(input_))
    n = len(input_)
    if input_ == rev_input_:
        return 0
    else:
        # 유사회문인지 검증
        if cnt < 1:
            go = 0
            back = n-1
            while go < back:
                # 좌우 대칭문자가 동일하면, 계속해서 좌측 += 1, 우측 -= 1
                if input_[go] == input_[back]:
                    go += 1
                    back -= 1
                # 좌우 대칭문자가 동일하지 않으면, cnt += 1
                else:
                    cnt += 1
                    left = ver(input_[go+1:back+1], cnt)  # 좌측부터 문자 하나씩 지울 때 ver 함수의 return 값을 left 객체에 저장
                    right = ver(input_[go:back], cnt)     # 우측부터 문자 하나씩 지울 때 ver 함수의 return 값을 right 객체에 저장
                    if min(left, right) == 0:  # 좌우 대칭문자 동일하지 않으면서, 좌측이나 우측 문자 하나 지울 때 return 0 나오면 == 유사회문(return 1) 
                        return 1
                    else: # 좌우 대칭문자 동일하지 않으면서, 좌측이나 우측 문자 하나 지울 때 return 0 안나오면 == 유사회문도 아님(return 2) 
                        return 2
        else:
            return 2    # cnt >= 1 인 경우, 즉 두 개 이상 문자를 지울 때
                    
t = int(input())
for i in range(t):
    input_ = list(input())
    res = ver(input_, 0)
    print(res)