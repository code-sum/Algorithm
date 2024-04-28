# 정보처리기사 C언어 기출문제



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



#### 2021년 3회

- 문제7. 다음 C언어로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오.)

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
