## Java 각종 코드

#### 클래스/메소드/변수 선언 관련

* **final**

```java
//PI는 3.14로 변하지 않는다.
//항상 변하지 않는 값을 만들고 싶을때 final 사용
//클래스에 사용시 상속 안됨, 메소드에 사용시 오버라이딩 안됨
final double PI = 3.14;
```



* **static**

```java
//클래스에서 static 변수/메소드를 선언하게 되면
//전역 변수/메소드로 만들수 있다.
static int var = 1;
```



* **abstract (추상)**

```java
abstract class A{
    //abstract 메소드는 안에 내용 구현 안하나 상속시 반드시 구현해야함
    public abstract int b();
    
    public void d() {
        System.out.println("Hi");
    }
}

class B extends A{
    public int b(){
        return 1;
    }
}
```



* **interface (인터페이스)**

```java
interface I{
    //상속시 메소드를 반드시 구현해야함
    public void z();
}

class A implements I{
    public void z(){
        System.out.println("Hi");
    }
}
```







#### 입출력

* **Scanner**

```java
//스캐너 변수 선언 생성
Scanner sc = new Scanner(System.in);
int i = sc.nextInt();
```







#### 반복문

* **for-each**

```java
String[] arr = {"1", "2", "3", "4", "5"};

//for-each 반복문
//배열 arr에서 항목 하나씩 가져와서 변수 s에 저장
for(String s : arr){
    System.out.println(s);
}
```







#### 상속

* **super**

```java
//부모클래스
class cl1 {
    int a;
    
    public cl1(int a){
        this.a = a;
    }
}


//자식클래스
class cl2 extends cl1 {
    int a,b;
    
    public cl2 (int a, int b){
        //super를 이용해서 부모클래스 생성자를 실행시킬수 있음.
        //중복된 코드 재활용의 의미
        super();
        this.b = b;
    }
}
```







#### 클래스 보안

* **Getter & Setter**

데이터가 외부에서 접근 할수 없게 하고, 메소드만 공개해 **외부에서 데이터에 직접 접근하는것을 막아야한다**.

클래스의 특성 중 하나인 **정보 은닉**을 잘 보여주는데, 사용하는 가장 큰 이유는 "**객체의 무결성**"을 보장하기 위함이다.

```java
class Student {
    private String name;
    private int age;
    
    public Student(String name, int age){
        this.name = name;
        this.age = age;
    }
    //Getter 메소드
    public String getName(){
        return name;
    }
    
    public int getAge(){
        return age;
    }
    
    //Setter 메소드
    public void setName(String name){
        this.name = name;
    }
    
    public void setAge(int age){
        this.age = age;
    }
}
```







#### 파일 쓰기/읽기/저장

* Buffer

```java
```







#### 기타

* **break, continue**

```java
for(int i=0; i<10; i++){
    if(i==3){
        //continue 사용시 밑에 남은 코드 실행안하고 뛰어 넘어서 다음 반복문 진행
        continue;
    } else if(i==7){
        //밑에 남은 코드 실행 안하고, 반복문 완전 종료
        break;
    }
    System.out.println(i);
}
```



* **this**

```java
class cl1 {
    int a,b;
    
    //생성자
    public cl1(int a, int b){
        //this는 본인 클래스(인스턴스)를 의미함
        this.a = a;
        this.b = b;
    }
}
```

