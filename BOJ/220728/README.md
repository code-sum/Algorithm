# 📌2022-07-28 BOJ 풀이



#### 1292. 쉽게 푸는 문제 [(link)](https://www.acmicpc.net/problem/1292)

> 동호는 내년에 초등학교를 입학한다. 그래서 동호 어머니는 수학 선행 학습을 위해 쉽게 푸는 문제를 동호에게 주었다.
>
> 이 문제는 다음과 같다. 1을 한 번, 2를 두 번, 3을 세 번, 이런 식으로 1 2 2 3 3 3 4 4 4 4 5 .. 이러한 수열을 만들고 어느 일정한 구간을 주면 그 구간의 합을 구하는 것이다.
>
> 하지만 동호는 현재 더 어려운 문제를 푸느라 바쁘기에 우리가 동호를 도와주자.

```python
# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 6 6 6 6 6 6 ... 의 수열을 상상하자

# 위 수열의 A, B구간이 주어짐
A, B = map(int, input().split())

data = []

for i in range(B+1):      # B까지 순회하는 반복문
    for j in range(i):      # append 작업을 어디서 멈출지 정하기 위해 작성한 이중반복문
        if B == len(data):
            break
        data.append(i)    # 처음부터 B구간까지에 해당하는 모든 요소를 data 에 붙여줌

print(sum(data[A-1:B]))   # 처음부터 A-1구간까지에 해당하는 요소들은 data 에서 제외하려고
                          # 인덱싱 처리를 하고, 남아있는 data 의 요소들을 sum


##############################################
################## 다른 코드 ##################
##############################################

# for문은 많은 탐색을 진행하기 때문에
# while문으로 탐색의 범위를 한정하는게 효율적이다!
# 수열을 만드는 문제는 시간 초과를 조심해야 하니까
# while문 이용해서 조건을 명확하게 잡는게 좋습니다.
```



#### 1302. 베스트셀러 [(link)](https://www.acmicpc.net/problem/1302)

> 김형택은 탑문고의 직원이다. 김형택은 계산대에서 계산을 하는 직원이다. 김형택은 그날 근무가 끝난 후에, 오늘 판매한 책의 제목을 보면서 가장 많이 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다.
>
> 오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.

```python
# 입력된 책 목록 중에 가장 많이 입력된 책 이름 출력


import sys
sys.stdin = open("1302.txt")

n = int(input())
list_ = {}

for i in range(n):
    input_ = input()
    if input_ not in list_:
        list_[input_] = 1
    else:
        list_[input_] += 1

freq_ = max(list_.values())
ans = []

for input_, num in list_.items():
    if num == freq_:
        ans.append(input_)

print(sorted(ans)[0])
```



#### 1357. 뒤집힌 덧셈 [(link)](https://www.acmicpc.net/problem/1357)

> 어떤 수 X가 주어졌을 때, X의 모든 자리수가 역순이 된 수를 얻을 수 있다. Rev(X)를 X의 모든 자리수를 역순으로 만드는 함수라고 하자. 예를 들어, X=123일 때, Rev(X) = 321이다. 그리고, X=100일 때, Rev(X) = 1이다.
>
> 두 양의 정수 X와 Y가 주어졌을 때, Rev(Rev(X) + Rev(Y))를 구하는 프로그램을 작성하시오

```python
# 첫번째 뒤집기를 쉽게 하기 위해 str으로 형 변환
X, Y = map(str, input().split())

# 뒤집기한 X, Y 를 int로 형 변환해서 더해줌 => 이후 str 으로 형 변환해서 뒤집기 한번 더 할 준비
tem = str(int(X[::-1]) + int(Y[::-1]))

print(tem[::-1])
```
