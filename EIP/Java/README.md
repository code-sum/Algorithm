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
  	public Static void main(String[] args) {
      Vehicle obj = new Car("Spark");
      System.out.print(obj.getName());
      }
  }
  ```

  - [답] Vehicle name : Spark



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

