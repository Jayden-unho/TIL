

[[_TOC_]]

<br>

---

# SQL 관련 각종 개념

## 객체

데이터베이스 내에 실체를 가지는 어떤것을 의미, 테이블이나 뷰, 인덱스 등 데이터베이스 안에 정의하는 모든 것을 일컫는 말

SELECT, INSERT 등은 객체를 조작하는 SQL 명령이고 객체라고는 할 수 없다.

대표적인 객체가 테이블인데, 테이블 내의 열이나 별명은 객체가 아니다. 



#### 스키마

데이터베이스 객체는 스키마라는 그릇 안에 만들어짐, 객체의 이름이 같아도 스키마가 서로 다르면 상관 없음

하나의 스키마 안에 여러개의 테이블이 들어가 있는 형태

데이터베이스에 테이블을 작성해서 구축해나가는 작업을 스키마 설계라고 부름

스키마는 SQL 명령의 DDL을 이용하여 정의 함



이름이 충돌하지 않도록 기능하는 그릇을 '네임스페이스' 라고 부르기도 함

<br>

---

## 물리 삭제와 논리 삭제

**물리 삭제**

* 데이터를 테이블에서 완전히 삭제

<br>

**논리 삭제**

* 삭제 유무를 의미하는 열 하나를 추가로 생성하여 데이터 삭제 여부를 논리적으로 표현함

  데이터 용량을 많이 차지하나, 상황에 따라 사용자가 삭제를 하여도 데이터 보존이 필요한 경우에 논리 삭제 이용

<br>

---

## 서브쿼리

SELECT, FROM, WHERE 명령으로 괄호를 묶어 지정

WHERE 에서 주로 사용됨

스칼라 서브쿼리가 사용하기 유용함

<br>

### DELETE 에서 사용

* DELETE FROM table_1 WHERE col_1 = (SELECT MIN(col_1) FROM table_1);

  1번 열이 최솟값인 행 삭제

### SELECT 에서 사용

* SELECT (SELECT COUNT(\*) FROM table_1) AS col_1, (SELECT COUNT(\*) FROM table_2) AS col_2 FROM DUAL;  -  (DUAL : 기본적으로 작성하는 새로운 테이블)

### SET 에서 사용

* UPDATE table_1 SET col_1 = (SELECT MAX(col_1) FROM table_1);

### FROM 에서 사용

특정 데이터베이스에서 LIMIT 와 유사한 기능 구현을 위해 사용

* SELECT * FROM (SELECT * FROM table_1) AS tb;
* SELECT * FROM (SELECT * FROM table_1 ORDER BY col_1 DESC) AS tb WHERE ROWNUM <= 2;

### INSERT 에서 사용

INSERT 에서는 꼭 스칼라 값일 필요는 없다

* INSERT INTO table_1 VALUES (SELECT COUNT(\*) FROM table_1), (SELECT COUNT(\*) FROM table_2);

<br>

---

## 상관 서브쿼리

* `EXISTS (SELECT 명령)`

  서브쿼리가 반환하는 결과값이 있는지 조사 가능

  예시)

  * UPDATE table_1 SET col_1 = 'test' WHERE EXISTS (SELECT * FROM table_2 WHERE col_2 = col_1);

    위의 쿼리에서 제일 마지막 조건문에서 col_2 는 table_2 에 속한 열이고, col_1 은 table_1 에 속한 열이다.

    EXISTS 술어에 서브쿼리 지정시 서브쿼리가 행을 반환할 경우에 참을 돌려주게됨

* `NOT EXISTS (SELECT 명령)`

  서브쿼리 반환 값이 없으면 참

  예시)

  * UPDATE table_1 SET col_1 = 'test' WHERE NOT EXISTS (SELECT * FROM table_2 WHERE table_2.col_2 = table_1.col_1);

    위의 쿼리와 비슷하나, 열이 명시적이지 않다. 그러나 이 쿼리는 `테이블명.열이름` 으로 표현하여 명시적으로 표현이 가능

<br>

## 집합

SELECT 명령을 실행하면 데이터베이스에 질의하여 그 결과 몇개의 행이 반환이 되는데, 이때 반환된 결과 전체를 하나의 집합이라고 생각하면 된다.

#### UNION

합집합 `SELECT UNION SELECT...` 형태로 사용함, 두개의 쿼리 뿐만 아니라 세개의 쿼리도 가능

OREDER BY 사용시에는 마지막 SELECT 에 사용한다.

교집합은 INTERSECT , 차집합은 EXCEPT (Oracle은 MINUS) 을 이용한다.

예시)

* SELECT * FROM table_1 UNION SELECT * FROM table_2;  -  중복값 제거됨
* SELECT * FROM table_1 UNION ALL SELECT * FROM table_2;  -  중복값 제거되지 않음

<br>

<br>

---

## 참고

서적 - [SQL 첫걸음](https://book.naver.com/bookdb/book_detail.nhn?bid=9738902)