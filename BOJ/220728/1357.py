# https://www.acmicpc.net/problem/1357



# 첫번째 뒤집기를 쉽게 하기 위해 str으로 형 변환
X, Y = map(str, input().split())

# 뒤집기한 X, Y 를 int로 형 변환해서 더해줌 => 이후 str 으로 형 변환해서 뒤집기 한번 더 할 준비
tem = str(int(X[::-1]) + int(Y[::-1]))

print(tem[::-1])