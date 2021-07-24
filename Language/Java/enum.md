## enum

#### 배경

enum은 열거형(enumerated type)이라고 부른다.

열거형은 서로 연관된 상수(변하지 않는 값)들의 집합이다.



#### 사용하는 이유

* 코드가 단순해진다.
* 인스턴스 생성과 상속을 방지한다.
* 키워드 enum을 사용하기 때문에 구현의 의도가 열거임을 분명하게 나타낼 수 있다.



#### 코드

```java
/*
class Fruit {
    public static final Fruit APPLE = new Fruit();
    public static final Fruit PEACH = new Fruit();
    public static final Fruit BANANA = new Fruit();
}

class Number {
    public static final Number ONE = new Number();
    public static final Number TWO = new Number();
    public static final Number THREE = new Number();
}
*/

//위의 코드와 동일한 내용들
enum Fruit {
    APPLE, PEACH, BANANA;
}

enum Number {
    ONE, TWO, THREE;
}
```

(enum에서는 상수 마지막에 세미콜론을 붙이지 않아도 컴파일이 가능)



#### 생성자/메소드/변수

enum은 사실 클래스이다. 그래서 생성자/메소드/변수를 가질 수 있다.

```java
enum Fruit {
    /*
    public static final Fruit APPLE = new Fruit();
    public static final Fruit PEACH = new Fruit();
    public static final Fruit BANANA = new Fruit();
    와 같은 코드이기에 생성자가 총 3번 실행이 된다
    */
    
    APPLE("red"), PEACH("pink"), BANANA("yellow");
    
    //변수와 생성자를 가질 수 있음
    public String color;
    Fruit(String color) {
        this.color = color;
    }
}
```

