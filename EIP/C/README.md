# 정보처리기사 C언어 기출문제



#### 2020년 1회 [1개 출제]

- 문제12. 다음은 C언어 소스 코드이다. 출력 결과를 쓰시오.

  ```c
  #include <stdio.h>
  
  void main() {
  	int i,j;
  	int temp;
  	int a[5] = {75,95,85,100,50};
    
  	for (i=0; i<4; i++) {
  		for (j=0; j<4-i; j++) {
  			if (a[j] > a[j+1]) {
  				temp = a[j];
  				a[j] = a[j+1];
  				a[j+1] = temp;
  			}
  		}
  	}
        
  	for (i=0; i<5; i++) {
  		printf("%d", a[i]);
  	}
  }
  ```

  - [답] 50758595100 (Bubble Sort 방식으로 오름차순 정렬된 배열의 원소들을 공백 없이 출력)



#### 2020년 3회 [2개 출제]

- 문제2. 다음은 C언어 소스 코드이다. 출력 결과를 쓰시오.

  ```c
  #include <stdio.h>
  
  void main() {
  	int i=0, c=0;
  	while (i<10) {
  		i++;
  		c*=i;
  	}
  	printf("%d",c);
  }
  ```

  - [답]  0  (c 는 0으로 선언된 상태이므로 어떤 수를 곱해도 0임)

- 문제13. 다음은 C언어 소스 코드이다. 출력 결과를 쓰시오.

  ```c
  #include <studio.h>
  
  int r1() {
  	return 4;
  }
  int r10() {
  	return (30+r1());
  }
  int r100() {
  	return (200+r10());
  }
  int main() {
  	printf("%d\n", r100());
  	return 0;
  }
  ```

  - [답] 234



#### 2020년 4회 [1개 출제]

- 문제18. 다음은 C언어 소스 코드이다. 출력값을 쓰시오.

  ```c
  #include <stdio.h>
  
  void main() {
  	char *p = "KOREA"
      printf("%s\n" , p);
      printf("%s\n" , p+3);
      printf("%c\n" , *p);
      printf("%c\n" , *(p+3));
      printf("%c\n" , *p+2);
  ```

  - [답] 
    - KOREA
    - EA
    - K
    - E
    - M



#### 2021년 1회 [1개 출제]

- 문제15. 다음은 C언어 프로그램이다. 실행 결과를 쓰시오.

  ```c
  #include <stdio.h>
  
  struct good {
  	char name[10];
  	int age;
  };
   
  void main() {
  	struct good s[] = {"Kim",28,"Lee",38,"Seo",50,"Park",35};
      
  	struct good *p;
  	p = s;
  	p++;
  	printf("%s\n", p-> name);
  	printf("%d\n", p-> age);
  };
  ```

  - [답] 
    - Lee
    - 38



#### 2021년 2회 [2개 출제]

- 문제16. 다음은 C언어 프로그램이다. 실행 결과를 쓰시오.

  ```c
  int main() {
  	int res;
  	res = mp(2,10);
  	printf("%d",res);
  	return 0;
  }
  
  int mp(int base, int exp) {
  	int res = 1;
  	for (int i=0; i < exp; i++) {
  		res = res * base;
  	}
  	return res;
  }
  ```

  - [답] 1024

- 문제18. 다음은 C언어 프로그램이다. 실행 결과를 쓰시오.

  ```c
  int main() {
  
  	int ary[3];
  	int s = 0;
  	*(ary+0)=1;
  	ary[1] = *(ary+0)+2;
  	ary[2] = *ary+3;
      
  	for (int i=0; i<3; i++) {
  		s=s+ary[i]
  	}
  
  	print("%d",s);
  
  }
  ```

  - [답] 8



#### 2021년 3회 [2개 출제]

- 문제12. 다음 C언어에 대한 알맞은 출력값을 쓰시오.

  ```c
  #include <stdio.h>
   
  int main() {
  	int *arr[3];
  	int a = 12, b = 24, c = 36;
  	arr[0] = &a;
  	arr[1] = &b;
  	arr[2] = &c;
   
  	printf("%d\n", *arr[1] + **arr + 1);
   
  }
  ```
  
  - [답] 37
  
- 문제17. 다음 C언어로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```c
  #include <stdio.h>
  
  struct jsu {
  	char nae[12];
      int os, db, hab, hhab;
  };
  
  int main() {
      struct jsu st[3] = {
          {"data1", 95, 88}, {"data2", 84, 91}, {"data3", 86, 75}
      };
      struct jsu* p;
      p = &st[0];
      
      (p+1)->hab = (p+1)->os + (p+2)->db;   // 159
      (p+1)->hhab = (p+1)->hab + p->os + p->db;   // 342
      
      printf("%d\n", (p+1)->hab + (p+1)->hhab);   // 501 (최종 정답, 159+342)
      
      return 0;
  }
  ```
  
  - 답 : 501 (159+342=501 이므로)



#### 2022년 1회 [3개 출제]

- 문제14. 다음은 C언어로 구현된 프로그램이다. 입력 값이 5일 때, 출력 값을 작성하시오.

  ```c
  #include <stdio.h>
  
  int func(int a) {
  	if (a <= 1) return 1;
  	return a * func(a - 1);
  }
   
  int main() {
  	int a;
  	scanf("%d", &a);
  	printf("%d", func(a));
  }
  ```

  - [답] 120 (5x4x3x2x1)

- 문제15. 다음은 C언어로 구현된 프로그램이다. 괄호 ( ) 안에 올바른 연산자를 써서 정수를 역순으로 출력하는 기능을 완성하시오. (단, 1230 처럼 0으로 끝나는 정수는 고려하지 않는다)

  ```c
  #include <stdio.h>
  
  int main() {
  	int number = 1234;
  	int div = 10, result = 0;
   
  	while (number ( 1. ) 0) {
  		result = result * div;
  		result = result + number ( 2. ) div;
  		number = number ( 3. ) div;
  	}
   
  	printf("%d", result);
  }
  ```

  - [답] 
    - (1)  !=  또는  > 
    - (2)  ÷  (나머지 연산자)
    - (3)  /  (몫 연산자)

- 문제17. 다음은 C언어로 구현된 프로그램이다. 알맞은 출력 값을 작성하시오.

  ```c
  #include <stdio.h> 
  
  int isPrime(int number) { 
  	int i; 
  	for (i=2; i<number; i++) { 
  		if (number % i == 0) return 0; 
  	} 
  	return 1; 
  } 
   
  int main(void) { 
  	int number = 13195, max_div=0, i; 
  	for (i=2; i<number; i++) {
  		if (isPrime(i) == 1 && number % i == 0) max_div = i;   
      }
  	printf("%d", max_div); 
  	return 0; 
  }
  ```

  - [답] 29



#### 2022년 2회 [3개 출제]

- 문제8. 다음 C언어로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```c
  #include <stdio.h> 
  
  struct A{ 
  	int n; 
  	int g;
  }; 
   
  int main() {
  	A a = new A[2] 
  	for (i=0; i <2; i++) {
  		a[i].n = i;
  		a[i].g = i+1;  
  	}
  	printf("%d", a[0].n + a[1].g);  
  }
  ```

  - [답] 2

- 문제15. 다음 C언어로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```c
  #include <stdio.h>
   
  int len(char* p);
   
  int main() {
  	char* p1 = "2022";
  	char* p2 = "202207";  
  	int a = len(p1);
  	int b = len(p2);
  	printf("%d", a + b);
  }
   
  int len(char* p) {
  	int r = 0;
  	while(*p != '\0'){
  		p++;
  		r++;
  	}
  	return r;
  }
  ```

  - [답] 10

- 문제16. 다음 C언어로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```c
  #include <stdio.h>
   
  int main(int argc, char *argv[]) {
  	int a[4] = {0, 2, 4, 8};
  	int b[3] = {};
  	int i = 1;
  	int sum = 0;
  	int *p1;
   
  	for (i; i < 4; i++) {
  		p1 = a + i;
  		b[i-1] = *p1 - a[i-1];
  		sum = sum + b[i-1] + a[i];
  	}
  	printf("%d", sum);
   
  	return 0;
  }
  ```

  - [답] 22



#### 2022년 3회 [2개 출제]

- 문제1. 다음 C언어로 구현된 프로그램을 분석하여 배열 `mines` 의 각 칸에 들어갈 값을 쓰시오.

  ```c
  #include <stdio.h>
  
  main() {
   
      int field[4][4] = {{0,1,0,1},{0,0,0,1},{1,1,1,0},{0,1,1,1}};
      int mines[4][4] = {{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}}; 
  	int w=4, h=4;
      
      for (int y=0; y<h; y++) {
          for (int x=0; x<w; x++) {
              if (field[y][x] == 0) continue;
              for (int j=y-1; j<=y+1; j++) {
                  for (int i=x-1; i<=x+1; i++) {
                      if (calculate(w,h,j,i)==1)
                          mines[j][i] += 1;
                  }
              }
          }
      }
      
      for (int y=0; y<h; y++) {
          for (int x=0; x<w; x++) {
              printf("%d", mines[y][x]);
          	printf("\n");
          }
      }
  }    
  
  
  int calculate(int w, int h,int j,int i) {
  	if (i>=0 && i<w && j>=0 && j<h) return 1;
  	return 0;
  }
  ```

  - 답 : 

    | 1    | 1    | 3    | 2    |
    | ---- | ---- | ---- | ---- |
    | 3    | 4    | 5    | 3    |
    | 3    | 5    | 6    | 4    |
    | 3    | 5    | 5    | 3    |

- 문제13. 다음 C언어로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```c
  #include <stdio.h>
  
  int main() {
      int s, el = 0;
      for (int i=6; i<=30; i++) {
          s=0;
          for (int j=1; j<=i/2; j++) {
              if (i%j == 0) {
                  s = s + j;
              }
          }
          if (s == i) {
              el++;
          }
      }
      printf("%d", el);
      return 0;  // main 함수는 int형을 반환해야 하므로 return 0을 추가
  }
  ```

  - [답] 2



#### 2023년 1회 [4개 출제]

- 문제2. 다음 C언어로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```c
  #include <stdio.h>
   
  int main() {
      char a[] = "Art";
      char* p = NULL;
      p = a;
   
      printf("%s\n", a);
      printf("%c\n", *p);
      printf("%c\n", *a);
      printf("%s\n", p);
   
      for(int i = 0; a[i] != '\0'; i++)
          printf("%c", a[i]);
  }
  ```

  - [답]
    - Art 
    - A 
    - A 
    - Art 
    - Art

- 문제3. 다음 C언어로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```c
  #include <stdio.h>
   
  int main() {
      char* a = "qwer";
      char* b = "qwtety";
   
      for (int i = 0; a[i] != '\0' ; i++) {
          for (int j = 0; b[j] != '\0'; j++) {
              if (a[i] == b[j]) printf("%c", a[i]);
          }
      }
  }
  ```

  - [답] qwe

- 문제9. 다음은 이진수를 십진수로 변환하는 C언어 코드이다. 괄호 (a) (b) 에 적합한 답을 작성하시오.

  ```c
  #include <stdio.h>
   
  int main() {
      int input = 101110;
      int di = 1;
      int sum = 0;
   
      while (1) {
          if (input == 0) break
          else {
              sum = sum + (input (a)(b)) * di;
              di = di * 2;
              input = input / 10;
          }
      }
      printf("%d", sum);
      return 0;
  }
  ```

  - [답]
    - (a) %    (b) 10 or 5 or 2
    - (a) &    (b) 1

- 문제14. 다음은 버블 정렬을 이용하여 배열에 저장된 수를 오름차순으로 정렬하는 프로그램이다. ①, ② 에 들어갈 알맞은 답을 쓰시오.

  ```c
  #include <stdio.h>
  
  void swap(int* a, int idx1, int idx2) {
      int t = a[idx1];
      a[idx1] = a[idx2];
      a[①] = t;
  }
  
  void Usort(int* a, int len) {
      for (int i = 0; i < len - 1; i++)
          for (int j = 0; j < len - 1 - i; j++)
              if (a[j] > a[j + 1])
                  swap(a, j, j + 1);
  }
  
  main() {
      int a[] = {85, 75, 50, 50, 100, 95};
      int nx = 5;
      Usort(a, ②);
  }
  ```

  - [답]  ① idx2   ② nx



#### 2023년 2회 [5개 출제]

- 문제1. 다음 C언어로 구현된 프로그램에 54321 을 입력시킨 결과가 43215일 때, <처리조건>을 참고하여 괄호에 들어갈 알맞은 식을 쓰시오.

  > <처리조건>
  >
  > - 괄호의 식에 사용할 문자는 다음으로 제한한다.
  > - n, i
  > - +, -, /, *, %
  > - 0~9, (, ), [, ]

  ```C
  #include <stdio.h>
  
  int main(void) {
      
      int n[5];
      int i;  
      
      for (i=0; i<5; i++) {
          printf("숫자를 입력해주세요 : ");
          scanf("%d", &n[i]);
      }
      
      for (i=0; i<5; i++) {   
          printf("%d", (   괄호   ));
      }
      
      return 0;
  }
  ```

  - [답] n[(i+1)%5]

- 문제3. 다음 C언어로 구현된 프로그램에 홍길동, 김철수, 박영희 가 순서대로 입력될 때, 알맞은 출력값을 쓰시오.

  ```c
  #include <stdio.h>
  #include <stdlib.h> 
  
  char n[30];
  char *test() {
      printf(입력하세요 : );
      gets(n);
      return n;
  }
   
  int main()
   
  {
      char * test1;
      char * test2;
      char * test3;
   
      test1 = test();
      test2 = test();
      test3 = test();
   
      printf("%s\n",test1);
      printf("%s\n",test2);
      printf("%s",test3);
   
  }
  ```

  - [답]
    - 박영희
    - 박영희
    - 박영희

- 문제5. 다음 C언어로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```c
  #include <stdio.h>
  
  int main() {
  	int n[3] = [73, 95, 82]; 
  	sum = 0;
      int i;
   
  	for (i=0; i<3; i++) {
  	    sum += n[i];
  	}
   
  	switch(sum/30) {
      	case 10:
      	case 9: 
              printf("A");
      	case 8: 
              printf("B");
      	case 7: 
      	case 6: 
              printf("C");
      	default: 
              printf("D");
  	}
      
      return 0;
  }
  ```

  - [답] BCD

- 문제7. 다음 C언어로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```c
  #include <stdio.h>
   
  int main() {
      int c = 0;
      for (int i=1; i<=2023; i++) { 
          if (i%4 == 0) c++; 
      }
      printf("%d", c);
  }
  ```

  - [답] 505

- 문제9. 다음 C언어로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```c
  #include <stdio.h>
  #define MAX_SIZE 10
   
  int arr[MAX_SIZE];
  int point= -1; 
   
  void into(int num) {
      if (point >= 9) printf("Full");
      arr[++point] = num;
  }
   
  int take() {
      if (isEmpty() == 1) printf("Empty");
      return arr[point--];
  }
   
  int isEmpty() {
      if (point == -1) return 1;
      return 0;
  }
   
  int isFull() {
      if (point == 9) return 1;
      return 0;
  }
   
  int main(int argc, char const *argv[]){
      int e;
      into(5); into(2);
      while(!isEmpty()){
          printf("%d", take());
          into(4); into(1); printf("%d", take()); 
          into(3); printf("%d", take()); printf("%d", take()); 
          into(6); printf("%d", take()); printf("%d", take()); 
      }
      return 0;
  }
  ```

  - [답] 213465 (스택 자료구조)

- 문제18. 다음 코드는 C언어로 선택정렬을 구현한 것이다. 오름차순으로 정렬할 경우 빈칸에 알맞는 연산자를 보기에서 골라 작성하시오.

  > <보기>   ...   <, <=, =>, >, ==, /, %

  ```c
  #include <stdio.h>
  
  int main() {
      int E[] = {64, 25, 12, 22, 11};
      int n = sizeof(E) / sizeof(E[0]);
      int i = 0;
      do {
          int j = i + 1;
          do {
              if (E[i] (   빈칸   ) E[j]) {  
                  int tmp = E[i];
                  E[i] = E[j];
                  E[j] = tmp;
              }
              j++;
          } while (j < n);
          i++;
      } while (i < n-1);
      for(int i=0; i<=n; i++)
          printf("%d", E[i]);
      return 0;
  }
  ```

  - [답] >



#### 2023년 3회 [4개 출제]

- 문제3. 다음 C언어로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```c
  #include
   
  int main() {
      char* p = "KOREA";
      printf("%s\n", p);
      printf("%s\n", p+1);
      printf("%c\n", *p);
      printf("%c\n", *(p+3));
      printf("%c\n", *p+4);
  }
  ```

  - [답] 
    - KOREA
    - OREA
    - K
    - E
    - O

- 문제4. 다음 C언어로 구현된 프로그램을 분석하여 괄호 () 에 적절한 기호를 쓰시오.

  > 출력결과: 
  > 10
  > 10

  ```c
  #include <stdio.h>
  #include <stdlib.h>
  
  typedef struct Data {
      char c;
      int *numPtr;
  } Data;
  
  int main() {
      int num = 10;
      Data d1;
      Data *d2 = malloc(sizeof(struct Data));
      
      d1.numPtr = &num;
      d2 (괄호) numPtr = &num;
  
      printf("%d\n", *d1.numPtr);
      printf("%d\n", *d2->numPtr);
  
      free(d2);
      return 0;
  }
  ```

  - [답] ->
    - 포인터가 가리키는 구조체의 멤버에 접근할 때는 **`->`** 연산자 사용

- 문제9. 다음 C언어로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```C
  #include <stdio.h>
  
  int test(int n) {
      int i, sum = 0;
      for (i = 1; i <= n / 2; i++) {
          if (n % i == 0)
              sum += i;
      }
      return n == sum;
  }
  
  int main() {
      int i, sum = 0;
      for (i = 2; i <= 100; i++) {
          if (test(i))
              sum += i;
      }
      printf("%d", sum);
      return 0;
  }
  ```

  - [답] 34

- 문제15. 다음 C언어로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```c
  #include <stdio.h>
  
  int f(int n) {
      if (n <= 1) return 1;
      else return n * f(n - 1);
  }
  
  int main() {
      printf("%d", f(7));
      return 0;
  }
  ```

  - [답] 5040



#### 2024년 1회 [4개 출제]

- 문제2. 다음 C언어로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```c
  #include <stdio.h>
  
  int main() {
      int v1 = 0, v2 = 35, v3 = 29;
  
      if (v1 > v2 ? v2 : v1) {
          v2 = v2 << 2;
      } else {
          v3 = v3 << 2;
      }
  
      printf("%d", v2 + v3);
  
      return 0;
  }
  ```

  - [답] 151

- 문제4. 다음 C언어로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```c
  #include <stdio.h>
  #include <string.h>
  
  void reverse(char* str) {
      int len = strlen(str);
      char temp;
      char* p1 = str;
      char* p2 = str + len - 1;
      while (p1 < p2) {
          temp = *p1;
          *p1 = *p2;
          *p2 = temp;
          p1++;
          p2--;
      }
  }
  
  int main(int argc, char* argv[]) {
      char str[100] = "ABCDEFGH";
  
      reverse(str);
  
      int len = strlen(str);
  
      for (int i = 1; i < len; i += 2) {
          printf("%c", str[i]);
      }
  
      printf("\n");
  
      return 0;
  }
  ```

  - [답] GECA

- 문제11. 다음 C언어로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```c
  #include <stdio.h>
  
  typedef struct {
      int accNum;
      double bal;
  } BankAcc;
  
  double sim_pow(double base, int year) {
      int i;
      double r = 1.0;
      for (i = 0; i < year; i++) {
          r = r * base;
      }
      return r;
  }
  
  void initAcc(BankAcc *acc, int x, double y) {
      acc->accNum = x;
      acc->bal = y;
  }
  
  void xxx(BankAcc *acc, double *en) {
      if (*en > 0 && *en < acc->bal) {
          acc->bal = acc->bal - *en;
      } else {
          acc->bal = acc->bal + *en;
      }
  }
  
  void yyy(BankAcc *acc) {
      acc->bal = acc->bal * sim_pow((1 + 0.1), 3);
  }
  
  int main() {
      BankAcc myAcc;
      initAcc(&myAcc, 9981, 2200.0);
      double amount = 100.0;
      xxx(&myAcc, &amount);
      yyy(&myAcc);
      printf("%d and %.2f", myAcc.accNum, myAcc.bal);
      return 0;
  }
  ```

  - [답] 9981 and 2795.10

- 문제19. 
