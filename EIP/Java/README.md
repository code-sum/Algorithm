# 정보처리기사 Java 기출문제



#### 2020년 1회 [2개 출제]

- 문제13. 다음은 자바 소스코드이다. 출력 결과를 쓰시오.

  ```java
  public class good {
  	public static void main (String[] args) {
      	int i;
        	int[] a = {0,1,2,3};
          for (i=0; i<4; i++) {
          	System.out.print(a[i] + " ");
          }
      }
  }
  ```

  - [답] 0 1 2 3

- 문제14. 다음은 자바 소스코드이다. 출력 결과를 쓰시오.

  ```java
  public class good {
  	public static void main (String[] args) {
  	int i = 3;
  	int k = 1;
  	swich (i) {
  		case 0;
  		case 1;
  		case 2;
  		case 3 k = 0;
  		case 4 k += 3;
  		case 5 k -= 10;
  		default: k--;
  	}
  	system.out.print(k);
  	}
  }
  ```

  - [답] -8 (switch case문에 break가 없음에 유의)



#### 2020년 2회 [2개 출제]

- 문제5. 다음은 자바 코드이다. 다음 밑줄에 들어갈 키워드를 쓰시오.

  ```java
  class parent
  	public void show() {
  		system.out.println("Parent");
  	}
  }
  
  class Child extends Parent {
  	public void show(){
  		system.out.println("Child");
  	}
  }
  
  public class good {
  	public static void main (String[] args) {
  		Parent pa = ____ Child();
  	    pa.show();
  	}
  }
  ```

  - [답] new

- 문제19. 다음은 자바 코드이다. 출력 결과를 쓰시오.

  ```java
  class A {
  	private int a;
  	public A (int a) {
  		this.a = a;
  	}
  	public void display () {
  		system.out.println("a=" + a);
  	}
  }
  
  class B extends A {
  	public B (int a) {
  		super(a);
  	    super.display();
      }
  }
  
  public class good {
  	public static void main (String[] args) {
  		B obj = new B(10);
  	}
  }
  ```

  - [답] a=10



#### 2020년 3회 [2개 출제]

- 문제15. 다음은 자바 코드이다. 출력 결과를 쓰시오.

  ```java
  abstract class vehicle{
  	private String name;
      abstract public String getName(String val);
      public String getName() {
      	return "vehicle name:" + name;
      }
  	public void setName(String val) {
      	name = val;
      }
  }
  
  class Car extends Vehicle {
  	public Car(String val) {
      	setName(val);
  	}
  public String getName(String val) {
  	return "Car name : " + val;
  	}
  public String getName(byte val[]) {
  	return "Car name : " + val;
  	}
  }
  
  public class good {
  	public Static void main (String[] args) {
      Vehicle obj = new Car("Spark");
      System.out.print(obj.getName());
      }
  }
  ```

  - [답] Vehicle name : Spark

- 문제17. 다음은 자바 코드이다. 출력 결과를 쓰시오.

  ```java
  public class good {
  	public static void main (String[] args) {
          int i=0;
          int sum=0;
          while (i<10) {
              i++;
              if (i%2 ==1)
                  continue;
              sum += i;
          }
  	System.out.println(sum);
  	}
  }
  ```

  - [답] 30



#### 2020년 4회 [3개 출제]

- 문제5. 다음은 n이 10일 때, 10을 2진수로 변환하는 자바 소스 코드이다. 1,2에 알맞은 값을 적으시오.

  > [출력결과] 00001010

  ```java
  class good {
  	public static void main (String[] args) {
  		int[]a = new int[8];
  		int i=0; int n=10;
  		while (   1.  ) {
          	a[i++] = (   2.  );
              n /= 2;
          }
          for (i=7; i>=0; i--) {
          	System.out.print(a[i]);
  		}
  	}
  }
  ```

  - [답] 
    - (1) n > 0 or n >=1 or i < 8 or i <= 7
    - (2) n%2 or n&1

- 문제6. 다음은 자바 소스 코드이다. 출력 결과를 보고 1,2에 알맞은 값을 적으시오.

  - [출력 결과] 
    - 1 4 7 10 13
    - 2 5 8 11 14
    - 3 6 9 12 15

  ```java
  public class good {
  	public static void main(String[] args) {
  		int[][]a = new int[(1.)][(2.)];
  		for (int i = 0; i <3; i++) {
  			for (int j=0; j < 5; j++) {
  				a[i][j] = j*3+(i+1);
  				System.out.print(a[i][j]+"");
  			}
  			System.out.println();
  		}
  	}
  }     
  ```

  - [답] 
    - (1) 3
    - (2) 5

- 문제19. 다음은 자바 소스 코드이다. 출력 결과를 쓰시오.

  ```java
  class parent {
  	public int compute(int num) {
  		if (num <= 1) return num;
  		return compute(num-1) + compute(num-2);
  	}
  }
   
  class Child extends parent {
  	public int compute(int num) {
  		if (num <= 1) return num;
  		return compute(num-1) + compute(num-3);
  	}
  }
     
  class good {
  	public static void main (String[] args) {
  		parent obj = new Child();
  		System.out.print(obj.compute(4));
  	}
  }
  ```

  - [답] 1



#### 2021년 1회 [2개 출제]

- 문제7. 다음 Java 프로그램 결과를 쓰시오.

  ```java
  public class good {
  	public static void main(String[] args) {
  		int[][]arr = new int[][]{{45,50,75},{89}};
  		System.out.println(arr[0].length);
  		System.out.println(arr[1].length);
  		System.out.println(arr[0][0]);
  		System.out.println(arr[0][1]);
  		System.out.println(arr[1][0]);
      }
  }
  ```

  - [답] 
    - 3
    - 1
    - 45
    - 50
    - 89

- 문제17. 다음은 Java 프로그램이다. 실행 결과를 쓰시오.

  ```java
  public class good {
  	public static void main(String[] args) {
  		int i, j;
  		for (j=0, i=0; i<=5; i++) {
  			j+=i;
  			System.out.print(i);
  			if (i==5) {
  				System.out.print("=");
  				System.out.print(j);
  			} else {
  				System.out.print("+");
  			}
  		}
  	}
  }
  ```

  - [답] 0 + 1 + 2 + 3 + 4 + 5 = 15



#### 2022년 3회

- 문제4. 다음 JAVA로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오.)

  ```java
  public class Test {
  	public static void main(String[] args) {
  		int result[] = new int[5];
  		int arr[] = { 77, 32, 10, 99, 50 };
          for (int i=0; i<5; i++) {
              result[i] = 1;
              for (int j=0; j<5; j++) {
                  if(arr[i] < arr[j]) {
                      result[i]++;
                  }
              }
          }
          for (int k=0; k<5; k++) {
              System.out.print(result[k]);
          }
      }
  }
  ```
  
  - [답] 24513

