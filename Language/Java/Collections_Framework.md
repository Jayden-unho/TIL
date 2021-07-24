## Collections Framework

#### 구조

![](https://github.com/unho-00/TIL/__Image/Java/1.jpg)
[그림보러가기](https://github.com/unho-00/TIL/blob/main/__Image/Java/1.jpg)








#### ArrayList (배열)

기존의 배열은 초기에 생성할때 몇개의 값을 다루는지 지정해주어야 한다.

중간에 배열의 값들이 추가 되거나 할때 단점들을 보완한게 **ArrayList** 이다. 

**ArrayList**는 기본적으로 내부에 어떠한 데이터 타입도 넣을 수 있다. (**Object** 타입으로 저장된다)



* **기본 코드**

  ```java
  //ArrayList 선언
  ArrayList arr = new ArrayList();
  //String만 담는 배열 선언
  ArrayList<String> arr2 = new ArrayList<String>();
  
  arr.add("one");	//값 추가
  arr.add("two");	//값 추가
  arr.size();		//arr.size() ArrayList의 길이 반환
  ```








#### Set (집합)

**Set**은 배열에서 중복을 허용하지 않는다. (중복된 데이터가 없음)

순서가 따로 정해져있지 않음 (ArrayList는 순서가 정해져있음)

대체로 **ArrayList**와 사용이 비슷



* **기본 코드**

```java
HashSet<Integer> A = new HashSet<Integer>();
A.add(1);
A.add(2);
A.add(3);

HashSet<Integer> B = new HashSet<Integer>();
B.add(3);
B.add(4);
B.add(5);

HashSet<Integer> C = new HashSet<Integer>();
C.add(1);
C.add(2);

//B나 C의 값들이 A의 값에 모두 포함이 되는가 (부분집합)
boolean re1 = A.containsAll(B); //false
boolean re2 = A.containsAll(C); //true

//B의 값들을 모두 A에 합친다 (합집합)
A.addAll(B);

//B의 값들 중 A에도 있는것만 남김 (교집합)
A.retainAll(B);

//A의 값들 중 B의 모든 값들을 뺀다 (차집합)
A.removeAll(B);
```







#### Map (사전형 Dictionary)

**key** 와 **value** 를 가짐

**key**값은 중복이 허용되지 않으나, **value**는 중복이 허용 됨



* **기본 코드**

```java
//선언, key와 value가 필요하므로 데이터 타입이 두개가 필요함
HashMap<String, Integer> a = new HashMap<String, Integer>();

//값 추가
a.put("one",1);	//key 값은 one, value 값은 1
a.put("two",2);
a.put("three",3);

String value1 = a.get("one");	//key값 one에 해당하는 value를 가져옴
```



* **모든 값 가져오기**

```java
//첫번째 방법
Set<Map.Entry<String, Integer>> entries = map.entrySet();
for(Map.Entry<String, Integer> entry : entries) {
    System.out.println(entry.getKey() + " : " + entry.getValue());
}


//두번째 방법
Set<Map.Entry<String, Integer>> entries = map.entrySet();
Iterator<Map.Entry<String, Integer>> i = entries.iterator();
while(i.hasNext()) {
    Map.Entry<String, Integer> entry = i.next();
    System.out.println(entry.getKey() + " : " + entry.getValue());
}
```

 







#### Iterator (반복자)

컨테이너에 담긴 값을 하나하나 꺼내서 처리할수있게 도와줌

```java
HashSet<Integer> A = new HashSet<Integer>();
A.add(1);
A.add(2);
A.add(3);

Iterator hi = A.iterator();
while(hi.hasNext()){	//hasNext() - 다음 값이 있다면 true
    System.out.println(hi.next());	//hi에 가지고 있는 값 빼내고, 사라짐
}
```







#### 정렬

* **Collections** 클래스를 이용하면 정렬할수있다.
  (단, 정렬하려는 객체(클래스)는 인터페이스 **Comparable**을 구현해야하고, 인터페이스 내 **compareTo**를 구현해야한다.)

```java
class Computer implements Comparable{	//Comparable을 반드시 구현해야함
    int serial;
    String owner;
    Computer(int serial, String owner){
        this.serial = serial;
        this.owner = owner;
    }
    public int compareTo(Object o) {	//compareTo를 구현해야함
        return this.serial - ((Computer)o).serial;	//serial 오름차순으로
    }
    public String toString(){
        return serial+" "+owner;
    }
}
 
public class CollectionsDemo {
     
    public static void main(String[] args) {
        List<Computer> computers = new ArrayList<Computer>();
        computers.add(new Computer(500, "egoing"));
        computers.add(new Computer(200, "leezche"));
        computers.add(new Computer(3233, "graphittie"));
        Iterator i = computers.iterator();
        System.out.println("before");
        while(i.hasNext()){
            System.out.println(i.next());
        }
        Collections.sort(computers);	//정렬
        System.out.println("\nafter");
        i = computers.iterator();
        while(i.hasNext()){
            System.out.println(i.next());
        }
    }
 
}
```

