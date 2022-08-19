# https://www.acmicpc.net/problem/1371

import sys
sys.stdin = open("1371.txt")

# 어떤 글이 주어졌을 때, 가장 많이 나온 글자를 출력

# std.stdin.readline() 이용해서 개행문자 \n 이 같이 입력받기
text = sys.stdin.read()

# 길이의 결과값을 저장할 리스트
# ord('a') 는 91, ord('z')는 122 값을 갖기 때문에(알파벳이 26글자)
# 크기가 26인 리스트를 생성
list_ = [0]*26

# 소문자이면, ord() 함수 이용해서 알파벳을 아스키코드로 바꾸기
# 아스키코드 97~122 는 알파벳 소문자 a~z
for i in text:
    if i.islower():
        # i가 알파벳 소문자에 해당하면 아스키코드로 바꿔서 a~z 를 표현한 리스트에 1씩 카운트
        list_[ord(i)-97] += 1

for j in range(26):

    # 1씩 카운트하던 값중에 max 가 등장하면
    # chr() 함수 이용해서 해당 아스키코드에 연동된 문자로 바꾸기
    if list_[j] == max(list_):

        # 출력값 여러 개일 경우 알파벳 순으로 앞서는 것부터 모두 '공백없이' 출력
        print(chr(j+97), end='')