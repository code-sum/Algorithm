# 문자열의 거울상

# 전체 테스트 케이스의 수
n = int(input())

for _ in range(1, n+1):
    
    # ‘b’, ‘d’, ‘p’, ‘q’로 이루어진 문자열을 리스트로 받음
    word = list(input())

    # 리스트의 요소들을 역순으로 배열
    reverse = word[::-1]

    # 각 요소들이 붙여서 출력될 수 있도록 .join() 활용
    Reverse = ''.join(reverse)

    print('#%d %s' % (_, Reverse))

