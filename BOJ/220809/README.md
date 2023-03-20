# 📌2022-08-09 BOJ 풀이



#### 1264. 모음의 개수 [(link)](https://www.acmicpc.net/problem/1264)

> 영문 문장을 입력받아 모음의 개수를 세는 프로그램을 작성하시오. 모음은 'a', 'e', 'i', 'o', 'u'이며 대문자 또는 소문자이다.

```python
import sys
sys.stdin = open("1264.txt")

# 입력은 여러 개의 테스트 케이스로 이루어져 있으며, 
# 각 줄마다 영어 대소문자, ',', '.', '!', '?', 공백으로 이루어진 문장

while True:
    text = input()
    if text == '#':
        break

    cnt = 0
    for i in text:
        if i in 'AEIOUaeiou':
            cnt += 1
    print(cnt)
```



#### 1371. 가장 많은 글자 [(link)](https://www.acmicpc.net/problem/1371)

> 영어에서는 어떤 글자가 다른 글자보다 많이 쓰인다. 예를 들어, 긴 글에서 약 12.31% 글자는 e이다.
>
> 어떤 글이 주어졌을 때, 가장 많이 나온 글자를 출력하는 프로그램을 작성하시오.

```python
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
```



#### 1526. 가장 큰 금민수 [(link)](https://www.acmicpc.net/problem/1526)

> 은민이는 4와 7을 좋아하고, 나머지 숫자는 싫어한다. 금민수는 어떤 수가 4와 7로만 이루어진 수를 말한다.
>
> N이 주어졌을 때, N보다 작거나 같은 금민수 중 가장 큰 것을 출력하는 프로그램을 작성하시오.

```python
N = int(input())

while True:

    # str(N)의 길이 = str(N)에서 4가 들어있는 개수 + 7이 들어있는 개수
    if len(str(N)) == str(N).count('4') + str(N).count('7'):
        print(N)
        break
    
    # N 에서 1씩 빼내려가면서 N보다 작거나 같은 조건값을 계속 추적
    N -= 1
```

