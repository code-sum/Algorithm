# BOJ I/O 처리

> 1. N개의 정수 입력 받기





#### 1. N개의 정수 입력 받기

```python
# 띄어쓰기로 구분된 데이터를 여러 개 입력 받을 때 (리스트에 담기)
sample = list(map(int, input().split()))

# 띄어쓰기로 구분된 데이터를 1~5개 이내로 입력 받을 때
A, B, C = map(int, input().split())
```

- 위 코드의 원리

  (1) `input()` : 사용자로부터 임의의 값을 입력 받고, 입력된 값을 문자열(str)로 인식

  ```python
  N = input("나이를 입력하세요: ")
  # 나이를 입력하세요: 
  ```

  (2) `int()` : 입력 값을 숫자(보통 int)로 인식해서 코드에 활용하고 싶을 때, `int()` 로 `input()` 을 감싸줌

  ```python
  N = int(input("나이를 입력하세요: "))
  print(N)
  
  # 나이를 입력하세요: 12
  # 12
  ```

  (3) `.split()` : 문자열을 띄어쓰기 단위로 나눠서 조각난 객체들이 담긴 리스트를 만듬

  ```python
  a = "저는 12살 입니다."
  print(a.split())
  
  # ['저는', '12살', '입니다.']
  ```

  ```python
  b = input().split()
  # 여기서 Terminal 에 '1 2 3 4' 를 입력하면
  
  print(b)
  # ['1', '2', '3', '4'] 출력
  ```

  ```python
  c, d = input().split()
  # 여기서 Terminal 에 '5 6' 을 입력하면
  
  print(c)
  # '5' 출력
  
  print(d)
  # '6' 출력
  ```

  ```python
  c, d = input().split()
  # 여기서 Terminal 에 '5 6' 을 입력하면
  
  x = int(c)
  y = int(d)
  
  print(x+y)
  # '11' 출력
  ```

  (4) map(한꺼번에 적용할 함수, 반복 가능한 자료형) : `input().split()` 이용하여 받은 문자열 c, d 를 정수형으로 변환할 때, `int()` 함수를 일일이 써주는 것은 번거롭고 비효율적이므로 `map()` 이용하여 한꺼번에 변환

  ```python
  A, B = map(int, input().split())
  # 여기서 Terminal 에 '11 22' 를 입력하면 
  
  print(type(A))
  # int
  
  print(type(B))
  # int
  
  print(A+B)
  # '33' 출력
  ```

  
