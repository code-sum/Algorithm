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



#### 2021년 3회

- 문제7. 다음 C언어로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

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
      
      printf("%d\n", (p+1)->hab = (p+1)->os + (p+2)->db);   // 159
      printf("%d\n", (p+1)->hhab = (p+1)->hab + p->os + p->db);   // 342
      printf("%d\n", (p+1)->hab + (p+1)->hhab);   // 501 (최종 정답, 159+342)
      
      return 0;
  }
  ```

  - 답 : 501 (159+342=501 이므로)



#### 2023년 2회

- 문제1. 다음 C언어로 구현된 프로그램에 54321 을 입력시킨 결과가 43215일 때, <처리조건>을 참고하여 괄호에 들어갈 알맞은 식을 쓰시오.
  
  > <처리조건>
  >
  > - 괄호의 식에 사용할 문자는 다음으로 제한한다.
  > - n, i
  > - +, -, /, *, %
  > - 0~9, (, ), [, ]
  ```C
  #include<stdio.h>
  
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
  - 답 : n[(i+1)%5]



#### 2022년 3회

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
