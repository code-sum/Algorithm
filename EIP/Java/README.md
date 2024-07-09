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
  	public void show() {
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



#### 2021년 2회 [2개 출제]

- 문제17. 다음은 Java 프로그램이다. 객체 생성 없이 사용할 수 있는 메소드를 정의하려면 빈 괄호 안에 무엇을 써야하는가?

  > 참고로 아래 코드 출력결과는 `positive` 이다.

  ```java
  public class Test {
  	public static void main(String[] args) {
  		System.out.print(Test.check(1));
  	}
     
  	public (  괄호  ) String check(int num) {
  		return (num >= 0) ? "positive" : "negative";
  	}
  }
  ```

  - [답] static

- 문제19. 다음은 Java 프로그램이다. 실행 결과를 쓰시오.

  ```java
  public class over1 {
  	public static void main(String[] args) {
  		ovr1 a1 = new ovr1();
  		ovr2 a2 = new ovr2();
  		System.out.println(a1.sun(3,2) + a2.sun(3,2));
  	}
      
  	int sun(int x, int y) {
  		return x + y;
  	}
  }
  
  class ovr2 extends ovr1 {
  
  	int sun(int x, int y) {
  		return x - y + super.sun(x,y);
  	}
  
  }
  ```

  - [답] 11



#### 2021년 3회 [2개 출제]

- 문제1. 다음 Java 코드에 대한 알맞은 출력값을 쓰시오.

  ```java
  class Connection {
  	private static Connection _inst = null;
  	private int count = 0;
  	static public Connection get() {
  		if (_inst == null) {
  			_inst = new Connection();
  			return _inst; 
  		}
  		return _inst;
  	}
  	public void count() { count ++; }
  	public int getCount() { return count; }
  }
   
  public class testcon {
  	public static void main(String[] args) {
  		Connection conn1 = Connection.get();
  		conn1.count();
  		Connection conn2 = Connection.get();
  		conn2.count();
  		Connection conn3 = Connection.get();
  		conn3.count();
      
  		System.out.print(conn1.getCount());
  	}
  }
  ```

  - [답] 3

- 문제11. 다음 Java 코드에 대한 알맞은 출력값을 쓰시오.

  ```java
  public class testco {
  	public static void main(String[] args) {
  		int a = 3, b = 4, c = 3, d = 5;
  		if ((a == 2 | a == c) & !(c > d) & (1 == b ^ c != d)) {
  			a = b + c;
  			if (7 == b ^ c != a) {
  				System.out.println(a);
  			} else {
  				System.out.println(b);
  			}
  		} else {
  			a = c + d;
  			if (7 == c ^ d != a) {
  				System.out.println(a);
  			} else {
  				System.out.println(d);
  			}
  		}
  	}
  }
  ```

  - [답] 7



#### 2022년 1회 [2개 출제]

- 문제3. 다음 Java 코드에 대한 알맞은 출력값을 쓰시오.

  ```java
  class A {
  	int a;
  	int b;
  }
    
  public class Main {
  	static void func1(A m) {
  	m.a *= 10;
  	}
    
  	static void func2(A m) {
  	m.a += m.b;
  	}
    
  	public static void main(String args[]) {
  		A m = new A();
  		m.a = 100;
  		func1(m);
  		m.b = m.a;
  		func2(m);
  		System.out.printf("%d", m.a);
  	}
  }
  ```

  - [답] 2000

- 문제11. 다음 Java 코드에서 밑줄에 들어갈 알맞은 코드를 작성하시오.

  ```java
  class Car implements Runnable {
  	int a;
  	public void run() {
  		system.out.println("message")
  	}
  }
    
  public class Main {
  	public static void main(String args[]) {
  		Thread t1 = new Thread(new _____());
  		t1.start();
  	}
  }
  ```

  - [답] Car



#### 2022년 2회 [2개 출제]

- 문제7. 다음 Java 로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```java
  public class Test {
  	public static void main(String args[]) {
    
  		int i = 3; int k = 1; 
  		switch(i) { 
  			case 1: k += 1;
  			case 2: k++;
  			case 3: k = 0; 
  			case 4: k += 3; 
  			case 5: k -= 10; 
  			default: k--; 
  		}
  		System.out.print(k); 
  	}
  }
  ```

  - [답] -8

- 문제17. 다음 Java 로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```java
  public class Conv { 
      int a;
  	public Conv(int a) {
  		this.a = a;
  	} 
  	int func() {
  		int b = 1; 
  		for (int i=1; i<a; i++) { 
  			b = a * i + b; 
  		}
  		return a + b;
  	}
  }
   
  public static void main(String[] args) {
  	Conv obj = new Conv(3);
  	obj.a = 5; 
  	int b = obj.func();
  	system.out.print(obj.a + b);
  	i
  }
  ```

  - [답] 61



#### 2022년 3회 [3개 출제]

- 문제4. 다음 Java 로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

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

- 문제19. 다음 Java 로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```java
  public class Main {
      static int[] mkarr() {
          int[] tempArr = new int[4];
          for (int i=0; i<tempArr.length; i++) {
              tempArr[i] = i;
          }
          return tempArr;
      }
      
      public static void main(String[] args) {
          int[] intArr;
          intArr = mkarr();
          for (int i=0; i<intArr.length; i++)
              System.out.print(intArr[i]);
      }
  }
  ```

  - [답] 0123

- 문제20. 다음 Java 로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```java
  public class Exam {
      public static void main(String[] args){
          int a = 0;
          for (int i=1; i<999; i++) {
              if(i%3==0 && i%2==0)
                  a = i;
          }
          System.out.print(a);
      }
  }
  ```

  - [답] 996



#### 2023년 1회 [3개 출제]

- 문제1. 다음 Java 로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```java
  class Static {
      public int a = 20;
      static int b = 0;
  }
   
  public class Main {
      public static void main(String[] args) {
          int a = 10;
          Static.b = a;
          Static st = new Static();
          System.out.println(Static.b++);
          System.out.println(st.b);
          System.out.println(a);
          System.out.print(st.a);
      }
  }
  ```

  - [답]
    - 10
    - 11
    - 10
    - 20

- 문제17. 다음 Java 로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  > 2020년 3회 15번 기출문제와 동일하게 출제
  
  ```java
  abstract class Vehicle {
      String name;
      abstract public String getName(String val);
      public String getName() {
              return "Vehicle name: " + name;
      }
  }
   
  class Car extends Vehicle {
      public Car(String val) {
              name=super.name=val;
      }
      public String getName(String val) {
              return "Car name:" + val;
      }
      public String getName(byte val[]) {
  		return "Car name : " + val;
  	}
  }
   
  public class Main {
      public static void main(String[] args) {
      Vehicle obj = new Car("Spark");
      System.out.println(obj.getName());
      }
  }
  ```
  
  - [답] Vehicle name: Spark

- 문제20. 다음 Java 로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```java
  class Parent {
      int x = 100;
      Parent() {
          this(500);
      }
      Parent(int x) {
          this.x = x;
      }
      int getX() {
          return this.x;
      }
  }
   
  class Child extends Parent {
      int x = 1000;
      Child() {
          this(5000);
      }
      Child(int x) {
          this.x = x;
      }
  }
   
  public class Main {
      public static void main(String[] args) {
          Child obj = new Child();
          System.out.println(obj.getX());
      }
  }
  ```

  - [답] 500



#### 2023년 2회 [2개 출제]

- 문제2. 다음은 JAVA 코드 문제이다. 가지고 있는 돈이 총 4620원일 경우 1000원, 500원, 100원, 10원의 지폐 및 동전을 이용하여 보기의 조건에 맞춰 최소한의 코드를 통해 괄호안을 작성하시오.

  > ```
  > 변수 : m
  > 연산자 : / , %
  > 괄호 : [ , ] , ( , )
  > 정수 : 1000, 500, 100, 10
  > ```

  ```java
  public class Problem {
      public static void main(String[] args) {
          m = 4620;
   
          a = (     (1)     );
          b = (     (2)     );
          c = (     (3)     );
          d = (     (4)     );
   
          System.out.println(a);
          System.out.println(b);
          System.out.println(c);
          System.out.println(d);
      }
  }
  ```

  - [답]
    - (1) m / 1000
    - (2) (m%1000) / 500
    - (3) (m%500) / 100
    - (4) (m%100) / 10

- 문제14. 다음 Java 로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```java
  public class Main {
      public static void main(String[] args) {
          String str1 = "Programming";
          String str2 = "Programming";
          String str3 = new String("Programming");
          
          System.out.println(str1==str2);
          System.out.println(str1==str3);
          System.out.println(str1.equals(str3));
          System.out.println(str2.equals(str3));
      }
  }
  ```

  - [답] 
    - true
    - false
    - true
    - true



#### 2023년 3회 [3개 출제]

- 문제1. 다음 Java 로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  ```java
  public class Main {
  	public static void main(String[] args) {
  		A b = new B();
  		b.paint();
  		b.draw();
  	}
  }
  
  class A {
  	public void paint() {
  		System.out.print("B");
  		draw();
  	}
  	public void draw() {
  		System.out.print("A");
  	}
  }
  
  class B extends A {
  	public void paint() {
  		super.paint();
  		System.out.print("C");
  		draw();
  	}
  	public void draw() {
  		System.out.print("D");
  	}
  }
  ```

  - [답] BDCDD

- 문제12. 다음 Java 로 구현된 프로그램을 실행하면 에러가 발생한다. 에러의 원인이 되는 코드라인이 몇 번인지 쓰시오.

  ```java
  class Person {
      private String name;
      public Person(String val) {
          name = val;
      }
      public static String get() {
      return name;
      }
      public void print() {
          System.out.println(name);
      }
  }
  public class main {
      public static void main(String[] args) {
          Person obj = new Person("Kim");
          obj.print();
      }
  }
  ```

  - [답] 7

- 문제14. 다음 Java 로 구현된 프로그램을 분석하여 그 실행 결과를 쓰시오. (단, 출력문의 출력 서식을 준수하시오)

  > 2020년 4회와 동일한 문제

  ```java
  class Parent {
  	int compute(int num) {
  		if(num <= 1)
  			return num;
  		return compute(num-1) + compute(num-2);
  	}
  }
  
  class Child extends Parent {
  	int compute(int num) {
  		if(num <= 1)
  			return num;
  		return compute(num-1) + compute(num-3);
  	}
  }
  
  public class main {
  	public static void main(String args[]) {
  		Parent obj = new Child();
  		System.out.print(obj.compute(7));
  	}
  }
  ```

  - [답] 2


