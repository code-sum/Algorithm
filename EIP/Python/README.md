# 정보처리기사 Python 기출문제



#### 2020년 2회 [1개 출제]

- 문제2. 다음은 Python 코드이다. 출력 결과를 쓰시오.

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

- 문제9. 다음은 Python 코드이다. 출력 결과를 쓰시오.

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

- 문제5. 다음은 Python 코드이다. 출력 결과를 쓰시오.

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



#### 2021년 2회 [1개 출제]

- 문제7. 다음은 Python 코드이다. 출력 결과를 쓰시오.

  ```python
  a = 100
  result = 0
  for i in range(1, 3):
      result = a >> i
      result = result + 1
  print(result)
  ```

  - [답] 26 (a 에 100 을 할당했을 때, 100을 오른쪽으로 1비트 시프트한 값은 50. 즉, 100을 2로 나눈 값)



#### 2021년 3회 [1개 출제]

- 문제14. 다음은 Python 코드이다. 출력 결과를 쓰시오.

  ```python
  a,b = 100, 200 
  print(a==b)
  ```

  - [답] False (앞글자가 대문자인 것에 유의)



#### 2022년 1회 [1개 출제]

- 문제6. 다음은 Python 코드이다. 출력 결과를 쓰시오.

  ```python
  def exam(num1, num2=2):
        print('a=', num1, 'b=', num2)
  exam(20)
  ```

  - [답] a= 20 b= 2



#### 2022년 2회 [1개 출제]

- 문제13. 다음은 Python 코드이다. 출력 결과를 쓰시오.

  ```python
  a = "REMEMBER NOVEMBER"
  b = a[:3] + a[12:16]
  c = "R AND %s" % "STR"
  print(b+c)
  ```

  - [답] REMEMBER AND STR



#### 2022년 3회 [1개 출제]

- 문제9. 다음 Python으로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단 출력문의 출력 서식을 준수하시오)

  ```python
  a = [1, 2, 3, 4, 5]
  a = list(map(lambda num : num + 100, a))
  print(a)
  ```

  - [답] [101, 102, 103, 104, 105]



#### 2023년 1회 [1개 출제]

- 문제15. 다음 Python으로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단 출력문의 출력 서식을 준수하시오)

  > 2020년 2회 2번 기출문제와 완전히 동일하게 출제

  ```python
  a = {'한국', '중국', '일본'}
  a.add('베트남')
  a.add('중국')
  a.remove('일본')
  a.update({'홍콩', '한국', '태국'})
  print(a)
  ```

  - [답] {'중국','한국','베트남','홍콩','태국'}  (순서 상관없이 요소 5개 빠짐없이 들어가면 됨)



#### 2023년 2회 [1개 출제]

- 문제19. 다음 Python으로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단 출력문의 출력 서식을 준수하시오)

  ```python
  a = "engineer information processing"
  b = a[:3]
  c = a[4:6]
  d = a[28:]
  e=b+c+d
  print(e)
  ```

  - [답] engneing



#### 2023년 3회 [1개 출제]

- 문제16. 다음 Python으로 구현된 프로그램과 <실행결과> 를 분석하여 괄호에 들어갈 알맞은 예약어를 쓰시오. (<실행결과> 첫 번째 라인의 '5 10' 은 입력받은 값에 해당한다.)

  > <실행결과>
  > x, y 값을 공백으로 구분하여 입력 : 5 10
  > x의 값 : 5
  > y의 값 : 10

  ```python
  x, y = input("x, y 값을 공백으로 구분하여 입력 :").(괄호)(' ')
  print("x의 값 :", x)
  print("y의 값 :", y)
  ```

  - [답] split



#### 2024년 1회 [1개 출제]

- 문제12.  다음 Python으로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단 출력문의 출력 서식을 준수하시오)

  ```python
  a = ["Seoul", "Kyeonggi", "Incheon", "Daejun", "Daegu", "Pusan"] 
  str01 = "S"
   
  for i in a:
      str01 = str01 + i[1]
   
  print(str01)
  ```

  - [답] Seynaau