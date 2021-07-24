## 객체지향의 이해

#### 클래스

* 객체 생성을 위한 청사진 또는 템플릿 (멤버와 관련된 추상 데이터 타입이 필요하다면)

1. 멤버 클래스 설계
2. 멤버 클래스 제작
3. 객체 생성 (프로그램 중심 역할)

```python
class 클래스명:	#클래스 정의
  pass


var = 클래스명()	#클래스의 객체 생성
```



* 생성자 메서드 : 객체를 생성하기 위해 호출하는
  \_\_init\_\_ 메서드
* 소멸자 메서드 : 객체가 소멸되기 전에 호출되는
  \_\_del\_\_ 메서드

```python
class 클래스명:
  def __init__(self, 매개변수 목록):
    pass
  
  #self를 제외한 매개변수는 사용하지 않음
  def __del__(self):
    pass
```



* 인스턴스 변수의 접근 제한 기능

  * Getter/Setter 메서드 제공 여부에 대한 고민 필요함

  ```python
  class Person:
    def __init__(self,name,age):
      #프라이빗 필드 생성
      self.__name = name
      self.__age = age
      
    def get_name(self):
      return self.name
    
    def get_age(self):
      return self.age
    
    def set_age(self, age):
      self.__age = age
  ```

  

* 파이썬에서는 getter/setter 대신할수있는 기능으로 **데코레이터(decorator)** 기능 제공함

  ```python
  class Person:
    def __init__(self,name,age):
      #프라이빗 필드 생성
      self.__name = name
      self.__age = age
      
    #변수처럼 사용 가능, __name 필드값을 반환하는 getter 메서드의 역할
    @property
    def name(self):
      return self.__name
    
    #변수처럼 사용 가능, __name 필드값을 반환하는 setter 메서드의 역할
    @age.setter
    def age(self, age):
      self.__age = age
  ```

  

* 클래스 메서드 - 클래스가 소유한 메서드

```python
class 클래스명:
  @classmethod
  def 클래스메서드(cls, 매개변수목록):	#cls - 클래스 자신에 대한 참조 전달
    pass
  
#클래스 메서드 사용
클래스명.클래스메서드(매개변수목록)
```



* 비교연산자 오버로딩

```python
class 클래스명:
  #self의 __age 필드가 other 객체의 __age 필드보다 크면 true 반환
  def __gt__(self, other):
    return self.__age > other.__age
  
  #self.__age 필드가 other.__age 필드보다 크거나 같으면 true 반환
  def __ge__(self, other):
    return self.__age >= other.__age
  
    #self.__age 필드가 other.__age 필드보다 작으면 true 반환
  def __lt__(self, other):
    return self.__age < other.__age
  
    #self.__age 필드가 other.__age 필드보다 작거나 같으면 true 반환
  def __le__(self, other):
    return self.__age <= other.__age
  
    #self.__age 필드가 other.__age 필드와 같으면 true 반환
  def __eq__(self, other):
    return self.__age == other.__age
  
    #self.__age 필드가 other.__age 필드와 다르면 true 반환
  def __ne__(self, other):
    return self.__age != other.__age
  
  
i=0
while True:
  #def __gt__(self,other): 메서드가 호출됨
  print(members[i] > members[i+1])
  i += 1
```



* \_\_str()\_\_ 메서드 - 함수에 객체를 전달해 문자열로 변환

```python
def __str__(self):
  return "{0}\t{1}".format(self.__name, self.__age)

for member in members:
  print(str(member))	#Person 클래스의 객체 전달하면 __str__ 메서드 호출
```

