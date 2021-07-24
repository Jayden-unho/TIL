## 함수

#### 언팩 연산자(*)

* 매개변수의 개수를 가변적으로 사용할 수 있도록 언팩 연산자(*) 제공

* 매개변수에 적용 시 인자를 튜플 형식으로 처리함

```python
#가변형 매개변수를 매개변수 중 가장 마지막에만 사용해야함
# ex) def calc(num, a, *params)
def calc(*params):	#값 1,2,3 이 튜플 형식으로 들어오게 됨
    total = 0
    for val in params:
        total += val
    return total

answer = calc(1,2,3)
```

```python
def calc(*params):	#값 1,2,3 이 튜플 형식으로 들어오게 됨
    total = 0
    count = 0
    for val in params:
        total += val
        count += 1
    return total, count

answer = calc(1,2,3) #값 여러개 반환 (튜플), answer = (total, count)
```



#### 키워드 언팩 연산자(**)

* 매개변수의 개수를 가변적으로 사용할 수 있도록 함
* 키워드 인자들을 전달해 매개변수를 딕셔너리 형식으로 처리함 (키1 = 값1, 키2 = 값2)

```python
def dict(**params):	#{'a':1, 'b';2, 'c':3} 과 같은 딕셔너리로 만들어짐
    pass

dict(a=1, b=2, c=3)
```



#### 기본 값을 갖는 매개변수

```python
def cal(a,b,operator="+"): #매개변수 뒤에 = 를 이용하면 기본값을 지정할 수 있다. 기본값 가지는 매개변수는 마지막에 사용
    if operator == "+:
        return x+y
    else:
        return x-y
    
answer = calc(1,2)	#기본값 사용
answer = calc(3,2,"-") #기본값 사용 안함
```





#### 중첩 함수 (함수 내에 중첩함수를 선언해 사용 가능)

* 중첩함수를 포함하는 함수 내에서만 호출이 가능함
* 중첩함수를 포함하는 함수의 스코프에도 접근이 가능함
* 함수 내에서 직접 선언해 호출할 수도 있고, 함수의 매개변수로 함수 인자를 전달받아 함수 내에서 호출해서 사용 가능

```python
def cal(func, x, y):	#함수를 매개변수로 받았기에, 
    return func(x,y)

def plus(op1, op2):
    return op1 + op2

def minus(op1, op2):
    return op1 - op2

cal(plus, 5, 10)	#인자값으로 plus 함수를 집어 넣음
```





#### 람다식 (람다 함수)

* Lambda 매개변수 : 반환값
* 변수에 저장해 재사용이 가능한 함수처럼 사용함
* 기존의 함수처럼 매개변수의 인자로 전달함
* 함수의 매개변수에 직접 인자로 전달함

```python
def cal(func, x, y):	#함수를 매개변수로 받았기에, 
    return func(x,y)

answer = cal(lambda a,b : a+b, 5, 10)

a = lambda a,b : a-b	#변수에 저장해서 사용 가능
answer2 = cal(a, 10, 5)
```



#### 클로저

* 중첩함수에서 중첩함수를 포함하는 함수의 scope에 접근 가능
* 중첩함수 자체를 반환값으로 사용한다면?
  * 정보 은닉 구현 가능
  * 전역변수의 남용 방지
  * 메서드가 하나밖에 없는 객체를 만드는 것보다 우아한 구현 가능

```python
def outer_func():
    id = 0 #지역변수 : 함수 내의 코드 또는 중첩함수에서만 접근 가능
    
    def inner_func():
        nonlocal id	#변수 id가 중첩함수인 inner_func 함수의 지역변수가 아님
        			#변수 id 접근시 outer_func 함수 스코프에서 찾게 만듦
        id += 1
        return id
    
    return inner_func	#inner_func() 함수 호출이 아닌 함수에 대한 참조를 반환함에 유의

make_id = outer_func()	#outer_func를 호출하면 inner_func이 반환되어 make_id는 함수가 된다.

print("결과 : {0}".format(make_id()))	#1
print("결과 : {0}".format(make_id()))	#2
print("결과 : {0}".format(make_id()))	#3
```

1. 중첩함수 inner_func() 호출
2. outer_func() 함수의 지역변수 id의 값 1씩 증가
3. 증가된 id 값 반환
4. str.format() 함수의 인자로 전달, 변환 문자열 생성
5. print() 함수를 통해 표준출력으로 출력





