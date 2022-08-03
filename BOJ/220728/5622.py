# https://www.acmicpc.net/problem/5622


# 전화기 번호별로 입력된 자판
key = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

# 문자열 입력(인덱스 추적을 위해 list 로 받음)
word = list(input())

# 1번(인덱스 0)은 3초, 2번(인덱스 1)은 4초, 3번(인덱스 2)은 5초 ...
time = 0

for i in word:
    for j in key:
        if i in j:
            time += key.index(j) + 3

print(time)


############################################################

# 딕셔너리를 이용한 방법

# 전화기 자판별로 걸리는 시간을 value에 입력
key = {
    "ABC": 3, 
    "DEF": 4, 
    "GHI": 5, 
    "JKL": 6, 
    "MNO": 7, 
    "PQRS": 8, 
    "TUV": 9, 
    "WXYZ": 10
}

word = input()
time = 0

for i in range(len(word)):
    for j in key.keys():    # .keys() 딕셔너리 key 목록이 담긴 dict_keys 반환
        if word[i] in j:    # 만약 word 의 i번째 문자가 key 중에 있다면
            time += key[j]  # 걸린 시간에 j번째 key 값(value), 다시 말하면 key 의 j번째 값(value)를 더해줌
                            # 작동원리: https://pythontutor.com/render.html#mode=display 참조
print(time)