# 정보처리기사 C언어 오답풀이



- [2023-2회] 문제 1. 다음 C언어로 구현된 프로그램에 54321 을 입력시킨 결과가 43215일 때, <처리조건>을 참고하여 괄호에 들어갈 알맞은 식을 쓰시오.
  > <처리조건>
  > - 괄호의 식에 사용할 문자는 다음으로 제한한다.
  > - n, i
  > - +, -, /, *, %
  > - 0~9, (, ), [, ]
  ```C
  #include<stdio.h>
  int main(void) {
    int n[] = {5, 4, 3, 2, 1};
    for (int i = 0; i < 5; i++)
        printf("%d", (   괄호   ));
  }
  ```
  - 답 : n[(i+1)%5]



- 다음 C언어 코드의 출력은?

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
