# https://www.acmicpc.net/problem/9012

import sys
sys.stdin = open("9012_input.txt")

# 테스트 케이스의 수
tc = int(input())

for i in range(tc):

    # '(' 와 ')' 로 이루어진 자료 input
    input_bracket = input()

    # '(' + ')' 모양이 완성되었을 때 이를 담아줄 리스트 생성
    done = []

    for j in input_bracket:

        # 괄호 열기'(' 는 done 에 일단 넣어줌
        if j == "(":
            done.append(j)

        # 괄호 닫기')' 는 done 을 검사
        elif j == ")":

            # 검사결과 done 이 비어있지 않으면 pop
            # 괄호열기 + 괄호닫기 완성의 결과가 pop 이므로
            if done:
                done.pop()

            # 검사결과 done 이 빈 상태면 "NO" 출력
            else:
                print("NO")
                break
    
    # 위의 for 문에서 break 발생한 적이 없으면?
    else:
        
        # 반복문 연산 결과 done 이 최종적으로 비어있는 상태라면
        # 짝이 모두 맞아 떨어져서 pop 된 상태기 때문에 "YES" 프린트
        if not done:
            print("YES")

        # done 안에 여전히 뭔가가 남아있으면 짝이 맞지 않으니 "NO" 프린트
        else:
            print("NO")