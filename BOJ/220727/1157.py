# https://www.acmicpc.net/problem/1157

# 변수.upper() = 변수에 있는 영어 소문자를 전부 대문자로 바꿈
word = input().upper()

# 주어진 word 에서 중복 값을 전부 제거하여 새로운 변수를 만듬
unique_word = list(set(word))

cnt_list = []
for i in unique_word:

    # A변수.count(B변수) = A변수에서 B변수 갯수를 세어라
    cnt = word.count(i)
    cnt_list.append(cnt)

# 가장 많이 사용된 알파벳이 여러 개면 "?" 출력
if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    max_index = cnt_list.index(max(cnt_list))
    print(unique_word[max_index])