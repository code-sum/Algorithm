# https://www.acmicpc.net/problem/1526

N = int(input())

while True:

    # str(N)의 길이 = str(N)에서 4가 들어있는 개수 + 7이 들어있는 개수
    if len(str(N)) == str(N).count('4') + str(N).count('7'):
        print(N)
        break
    
    # N 에서 1씩 빼내려가면서 N보다 작거나 같은 조건값을 계속 추적
    N -= 1