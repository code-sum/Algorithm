# https://www.acmicpc.net/problem/2902

import sys
sys.stdin = open("2902_input.txt")

# 긴 형태의 알고리즘 이름이 주어졌을 때, 
# 이를 짧은 형태로 바꾸어 출력하는 프로그램을 작성하시오.

# "-" 로 구분되는 긴 이름 입력
name = list(input().split("-"))

# 짧아진 이름 붙여줄 변수 선언
short_name = ""

for i in name:

    # "-" 이후 첫번째로 등장하는 문자들을 short_name 에 붙이기
    short_name += i[0]        

print(short_name)