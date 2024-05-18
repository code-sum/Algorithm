# 정보처리기사 Python 기출문제



#### 2020년 2회 [1개 출제]

- 문제2. 다음은 파이썬 코드이다. 출력 결과를 쓰시오.

  ```python
  a = {'일본','중국','한국'}
  a.add('베트남')
  a.add('중국')
  a.remove('일본')
  a.update(['홍콩','한국','태국'])
  print(a)
  ```

  - [답] {'중국','한국','베트남','홍콩','태국'}  (순서 상관없이 요소 5개 빠짐없이 들어가면 됨)



#### 2020년 4회 [1개 출제]

- 문제9. 다음은 파이썬 코드이다. 출력 결과를 쓰시오.

  ```python
  lol = [[1,2,3],[4,5],[6,7,8,9]]
  print(lol[0])
  print(lol[2][1])
  for sub in lol:
  	for item in sub:
          print(item, end = '')
  	print()
  ```

  - [답]
    - [1,2,3]
    - 7
    - 123
    - 45
    - 6789



#### 2021년 1회 [1개 출제]

- 문제5. 다음은 파이썬 코드이다. 출력 결과를 쓰시오.

  ```python
  class good :
  	li = ["seoul", "kyeonggi", "inchon", "daejeon", "daegu", "pusan"]
  
  g = good()
  str01 = ''
  for i in g.li:
  	str01 = str01 + i[0]
      
  print(str01)
  ```

  - [답] skiddp



#### 2022년 3회

- 문제9. 다음 Python으로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단 출력문의 출력 서식을 준수하시오.)

  ```python
  a = [1, 2, 3, 4, 5]
  a = list(map(lambda num : num + 100, a))
  print(a)
  ```

  - [답] [101, 102, 103, 104, 105]