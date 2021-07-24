## 제네릭(Generic)

제네릭(Generic)은 클래스 내부에서 사용할 데이터 타입을 외부에서 지정하는 기법이다.



#### 자주 사용하는 타입인자

| 타입인자 | 설명    |
| :------- | :------ |
| \<T\>      | Type    |
| \<E\>      | Element |
| \<K\>      | Key     |
| \<N\>      | Number  |
| \<V\>      | Value   |
| \<R\>      | Result  |



#### 코드

```java
class Person <T> {
    //변수 데이터 타입은 제네릭으로 외부에서 지정하는거에 따라 변한다
    public T info;
}

public static void main(String[] args) {
    //외부에서 인스터스화할때 타입을 String으로 지정하여 T의 데이터 타입은 String이 된다.
    Person<String> p1 = new Person<String>();
    //외부에서 인스터스화할때 타입을 StringBuilder로 지정하여 T의 데이터 타입은 StringBuilder가 된다.
    Person<StringBuilder> p2 = new Person<StringBuilder>();
}
```

  

#### 다중 타입 사용

```java
class EmployeeInfo{
	public int rank;
	EmployeeInfo(int rank){
		this.rank = rank;
	}
}

//T,S 는 참조형 데이터만 올 수 있음, 기본형 데이터 타입(int,double,char...)는 안됨
//기본형 데이터 타입을 넣기 위해서는 래퍼클래스(wrapper class) 사용해야함, 기본 데이터 타입을 참조형인거처럼 만든것임
class Person<T, S> {
	public T info;
	public S id;
	
	public Person(T info, S id) {
		this.info = info;
		this.id = id;
	}
    
    //메소드에서도 제네릭 사용 가능
    public <U> void printInfo(U info){
        System.out.println(info);
    }
}

public class test {
	public static void main(String[] args) {
		Integer id = new Integer(1);
		EmployeeInfo rank = new EmployeeInfo(1);
		Person<EmployeeInfo, Integer> p1 = new Person<EmployeeInfo, Integer>(rank, id);
        //생략 가능
        //Person p1 = new Person(rank, id);
		System.out.println(p1.info);
		System.out.println(p1.id.intvalue());
        
        
        p1.<EmployeeInfo>printInfo(e);
        //생략 가능
        //p1.printInfo(e);
	}

}
```





#### 제네릭의 제한

제네릭은 외부에서 어떤 타입을 넣어주냐에 따라 변하기 때문에 어떠한 타입이든지 다 들어올수 있다.

그래서 이러한 타입을 제한해서 사용할 수 있다.

```java
interface Info {
    int getLevel;
}

class EmployeeInfo implements Info {
    public int rank;
    EmployeeInfo(int rank){
        this.rank = rank;
    }
    public int getLevel(){
        return this.rank;
    }
}

//제네릭 타입 옆에 extends를 사용하면 해당 클래스/인터페이스이거나 그 클래스/인터페이스의 자식 클래스/인터페이스만 들어오게 제한한다.
class Person<T extends Info>{
    public T info;
    Person(T info){
        this.info = info;
        //위에서 T extends Info 를 하였기 때문에 인터페이스 Info의 변수나 메소드 호출 가능
        info.getLevel();
    }
}
```





#### 제네릭 와일드 카드

**?**는 와일드카드라 부른다.

* **<? extends T>** : 와일드카드의 상한 제한 - T와 그 자손들을 구현한 객체들만 매개변수로 가능
* **<? super T>** : 와일드카드의 하한 제한 - T와 그 조상들을 구현한 객체들만 매개변수로 가능
* **<?>** : 제한 없음
