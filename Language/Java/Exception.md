## Java Exception

#### 예외의 종류

* **ArithmeticException** : 수학적 예외 발생
* **ArrayIndexOutOfBoundsException** : 배열 인덱스 범위 초과
* **FileNotFoundException** : 파일을 찾을 수 없음
* **IOException** : 입출력 예외
* **IllegalArgumentException** : 적합하지 않은 인자가 들어옴
* **IllegalStateException** : 메소드를 호출하기 위한 상태가 아님
* **NullPointerException** : 매개 변수 값이 null 일때





#### 예외 발생 사용 코드

* **try-catch-finally**

```java
try {
    //실행 코드
} catch(Exception e) {
    //오류 발생시 실행 코드
    System.out.println(e.getMessage()); //오류의 가장 간단한 정보만 출력
    System.out.println(e.toString()); //오류의 조금 더 자세한 정보 출력
    e.printStackTrace(); //오류에 관한 모든 내용 출력
} finally {
    //예외가 발생하든 안하든 무조건 실행되는 코드
}
```



* **throws**

```java
class B {
    void method() throws ArithmeticException { //사용자에게 예외 사항 넘김
        //0으로 나누어 예외 발생
        int result = 3/0;
    }
}

class C {
    void method() throws ArithmeticException { //사용자에게 예외 사항 넘김
        B b = new B();
	    b.method()
    }
}

public class main{
    public static void main(String[] args) {
        C c = new C();
        try {
            c.method();
        } catch(Exception e) {
            //예외 발생시 실행 코드
        }
    }
}
```

main클래스는 C클래스의 method() 사용자, C클래스는 B클래스의 method() 사용자이다.

B클래스 method()는 예외 사항을 사용자 C에게 넘기고, C의 method()는 예외 사항을 사용자 main에게 넘겼다.

마지막에 main에서 예외사항을 처리함

(예외는 하나가 아니라 여러개 넘길 수 있음)





#### 예외 종류별 대응하는 법

```java
//예외
try {
    //실행 코드
} catch(ArithmeticException e) {
    //수학적예외 예외 발생시 실행되는 코드
} catch(ArrayIndexOutOfBoundsException e) {
    //배열 인덱스 범위 초과 예외 발생시 실행되는 코드
} catch(Exception e) {
    //전체 예외 발생시 실행되는 코드
}
```

다중 **catch**를 사용하여 오류별로 대응할수있다.

**catch**에서 전체 예외를 걸러내는 **Exception** 부분은 **catch**문 제일 마지막에 넣는다.





#### 예외 만들기

```java
void divide(int a, int b) {
    if(b == 0){
        //분모가 0인 경우에, 예외를 만들어 낸다
        throw new IllegalArgumentException("두번째 값이 0이 될수 없습니다.");
    }
    int result = a/b;
}
```





#### 예외간 차이 (checked & unchecked)

예외클래스의 부모클래스의 차이에 따라 발생한다

* **ArithmeticException 의 경우**
  java.lang.Object
  	java.lang.Throwable
  		java.lang.Exception
  			java.lang.RuntimeException
  				java.lang.ArithmeticException
  부모클래스 중 RuntimeException 이 존재 (**unchecked**)
* **IOException 의 경우**
  java.lang.Object
      java.lang.Throwable
          java.lang.Exception
              java.io.IOException
  부모클래스 중 RuntimeExeption 이 존재하지 않음 (**checked**)

**checked**의 경우에는 반드시 try~catch 또는 throws를 이용해서 예외를 처리하여야 함.

**unchecked**의 경우에는 꼭 처리하지 않아도 됨