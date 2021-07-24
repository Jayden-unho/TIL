## 예외처리

#### 예외 발생시 해결 방법

* **if 문을 이용한 예외의 처리**
  정상적인 흐름을 제어할 경우에만 사용 가능
* **try~except 문을 이용한 예외의 처리**
  1. 예외가 발생했을때 처리
* **try~except~else 문을 이용한 예외의 처리**
  1. 예외가 발생했을때 처리
  2. 예외가 발생하지 않았을때
* **try~except~else~finally 문을 이용한 예외의 처리**
  1. 예외가 발생했을때 처리
  2. 예외가 발생하지 않았을때
  3. 예외 발생과 상관없이 실행



#### 예외 객체 - 코드를 실행 중 오류가 발생하면 만들어진 것으로, 오류 발생과 관련한 정보를 가지고 있음

```python
try:
    pass
except Exception as ex: #Exception 예외, 객체 ex 에 담음
    pass



#아래와 같이 에러 종류별로 처리할수도 있다
try:
    pass
except ValueError as ve: #ValueError 예외, 객체 ex 에 담음
    pass
except ZeroDivisionError as ze: #ZeroDivisionError 예외, 객체 ex 에 담음
    pass
except Exception as ex: #Exception 예외(모든 예외), 객체 ex 에 담음
    pass
```



#### 강제 예외 발생 - 특정 조건에서 예외 객체를 만들어 예외를 일으킬 수 있음

```python
def calc(a, b):
    if a.isdigit() and b.isdigit():
        return int(a) * int(b)
    else:
        raise ValueError("숫자가 아닌 값이 입력되었습니다.") #raise 문을 이용해서 강제로 ValueError 예외 상황 일으킴
        
        
try:
    calc('1',1)
except ValueError as ve: #위에서 오류 발생시 ValueError에서 걸림
    pass
except ZeroDivisionError as ze: 
    pass
except Exception as ex: 
    pass
```





#### raise 와 assert 비교

| 비교                    | raise 문    | assert 문            |
| ----------------------- | ----------- | -------------------- |
| 용도                    | 예외의 발생 | 상태의 검증          |
| 언제 예외를 일으키는가? | 항상        | 검증식이 거짓일 때만 |
| 어떤 예외를 일으키는가? | 지정한 예외 | `AssertionError`     |

raise 문은 오류를 이미 발견한 상황에서 예외를 발생시키기 위한 명령이다. 따라서 무조건 예외 발생시킴

그에 반해 assert는 상태 검증하기 위한 명령이다. 지정한 검증식을 계산하여 결과가 참일때는 아무것도 하지 않고, 결과가 거짓일때만 AssertionError 발생시킨다.

```python
# raise
raise 예외클래스('메시지')

# assert
assert 검증식(표현식 (ex)if문 조건), '오류메시지'
```

