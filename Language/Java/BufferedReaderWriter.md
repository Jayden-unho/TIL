## Java BufferedReader / BufferedWriter

#### BufferedReader

* Scanner(Space와 Enter를 모두 경계로 인식)와 다르게 BufferedReader는 Enter만 경계로 인식하고 받은 데이터가 String으로 고정 됨

**사용법**

```java
BufferedReader bf = new BufferedReader(new InputStreamReader(System.in)); //선언
String s = bf.readLine(); //String
int i = Integer.parseInt(bf.readLine()); //Int
```

**주의점**

1. readLine() 시 리턴값을 String으로 고정되기에 String이 아닌 다른 타입으로 입력을 받으려면 형변환을 꼭 해야함
2. 예외처리를 항상 해주어야 함



#### Read한 데이터 가공

```java
StringTokenizer st = new StringTokenizer(s); //StringTokenizer인자값에 입력 문자열 넣음
int a = Integer.parseInt(st.nextToken()); //첫번째 호출
int b = Integer.parseInt(st.nextToken()); //두번째 호출

String array[] = s.split(" "); //공백마다 데이터 끊어서 배열에 넣음
```

Read한 데이터는 Line단위로만 나눠져 공백단위로 데이터 가공 위해서 따로 작업 필요

**방법**

1. StringTokenizer 사용
   nextToken() 함수를 쓰면 readLine()을 통해 입력받은 값을 공백단위로 구분하여 순서대로 호출 가능
2. String.split() 함수를 활용하여 배열에 공백단위로 끊어서 데이터를 넣고 사용하는 방식





#### BufferedWriter

많은 양의 출력에서는 입력과 마찬가지로 System.out.print() 보다 효율적

```java
BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));//선언
String s = "abcdefg";//출력할 문자열
bw.write(s);//출력
bw.newLine(); //줄바꿈
bw.flush();//남아있는 데이터를 모두 출력시킴
bw.close();//스트림을 닫음
```

버퍼를 잡아 놓았기 때문에 반드시 flush() / closse()를 반드시 호출해 뒤처리를 해야함

write() 에는 자동 개행기능이 없어 \n을 통해 따로 처리해주어야 함

(newLine()으로 줄바꿈 가능)





#### 주요 메서드

| 메서드명                                       | 기능                                                         |
| ---------------------------------------------- | ------------------------------------------------------------ |
| BufferedReader(Reader rd)                      | rd에 연결되는 문자입력 버퍼스트림 생성                       |
| BufferedWriter(Writer wt)                      | wt에 연결되는 문자출력 버퍼스트림 생성                       |
| int read()                                     | 스트림으로부터 한 문자를 읽어서 int 형으로 리턴              |
| int read(char[] buf)                           | 문자배열 buf의 크기만큼 문자를 읽어들임. 읽어들인 문자 수를 리턴 |
| int read(char[] buf, int offset, int length)   | buf의 offset위치에서부터 length 길이만큼 문자를 스트림으로부터 읽어들임 |
| String readLine()                              | 스트림으로부터 한 줄을 읽어 문자열로 리턴                    |
| void mark()                                    | 현재우치를 마킹, 차 후 reset() 을 이용하여 마킹위치부터 시작함 |
| void reset()                                   | 마킹이 있으면 그 위치에서부터 다시시각, 그렇지 않으면 처음부터 다시시작 |
| long skip(int n)                               | n 개의 문자를 건너 뜀                                        |
| void close()                                   | 스트림 닫음                                                  |
| void write(int c)                              | int 형으로 문자 데이터를 출력문자스트림으로 출력             |
| void write(String s, int offset, int length)   | 문자열 s를 offset 위치부터 length 길이만큼을 출력스트림으로 출력 |
| void write(char[] buf, int offset, int length) | 문자배열 buf의 offset 위치부터 length 길이만큼을 출력스트림으로 출력 |
| void newLine()                                 | 줄바꿈 문자열 출력                                           |
| void flush()                                   | 남아있는 데이터를 모두 출력시킴.                             |



---

[사이트 참고](https://coding-factory.tistory.com/251)