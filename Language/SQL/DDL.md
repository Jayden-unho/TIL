[[_TOC_]]

<br>

# SQL_DDL (Data Definition Language)

스키마 내의 객체(테이블, 뷰 등..)를 관리할때 사용됨

## 1️⃣ 명령어

### CREATE

객체를 생성할때 사용함

`CREATE TABLE table_1 (열 정의1, 열 정의2, ...)` 형태로 사용함

위치 - 맨 앞에 사용

<br>

예시)

* CREATE TABLE table_1 (col_1 INTEGER NOT NULL DEFAULT 0, col_2 TEXT NOT NULL);

<br>

### DROP

객체를 삭제할때 사용함

`DROP TABLE table_1` 형태로 사용함

위치 - 맨 앞에 사용

참고

* TRUNCATE TABLE table_1;
  사용시 테이블은 그대로 두고, 전체 데이터를 삭제함 (DELETE 보다 조금 더 빠름)

<br>

예시)

* DROP TABLE table_1;

<br>

### ALTER

테이블을 변경할때 사용함

`ALTER TABLE table_1 변경명령` 형태로 사용함

위치 - 맨 앞에 사용

<br>

예시)

* ALTER TABLE table_1 ADD col_5 INTEGER NOT NULL DEFAULT 0;  -  새로운 열을 추가할때 (기존에 데이터가 있으면 이전 데이터에 새로 추가된 열에 어떠한 값을 넣을지 DEFAULT 로 정해주어야 함)
* ALTER TABLE table_1 MODIFY col_1 INTEGER DEFAULT 10;  -  해당 열의 데이터형테 기본값, 제약 등을 변경
* ALTER TABLE table_1RENAME table_new;  -  테이블 이름 바꿈
* ALTER TABLE table_1 CHANGE col_1 col_new TEXT;  -  테이블 열 이름 바꿈 col_1 -> col_new 를 텍스트 자료형으로
* ALTER TABLE table_1 DROP col_3;  -  열 삭제

<br>

<br>

---

## 2️⃣ 개념

### 제약

`CONSTRAINT 키워드 제약명령 (열1, 열2...)` 형태로 사용

제약의 종류

* NOT NULL

  열 값으로 NULL 값이 들어올 수 없음

* UNIQUE

  열 값으로 중복을 허용하지 않음

* PRIMARY KEY

  기본키로 행 하나에 하나의 키 값으로 NOT NULL 제약과 UNIQUE 제약 속성을 모두 가지고 있음

<br>

예시)

* CREATE TABLE table_1 (col_1 INTEGER `NOT NULL`, col_2 INTEGER `NOT NULL`, col_3 TEXT, `CONSTRAINT pk PRIMARY KEY (col_1, col_2)`);
* ALTER TABLE table_1 MODIFY col_1 TEXT NOT NULL;  -  기존 열의 제약 추가
* ALTER TABLE table_1 ADD CONSTRAINT pk PRIMARY KEY (col_1);  -  기존 테이블에 기본키 제약 추가 (단, 테이블 당 기본키는 하나만 가능)
* ALTER TABLE table_1 MODIFY col_1 TEXT;  -  기존 열의 제약 삭제 (NOT NULL을 안넣으면 삭제됨)
* ALTER TABLE table_1 DROP CONSTRAINT pk;  -  기존 테이블 제약 삭제 (제약명으로 삭제 가능)

<br>

### 인덱스

인덱스를 만들어, 원하는 자료를 조금 더 빠르게 찾을 수 있음

테이블의 크기에 따라 인덱스 작성시간도 달라짐

Oracle, DB2 등에서는 인덱스는 스키마 객체, MySQL, SQLServer 는 테이블 내의 객체가 됨

`CREATE INDEX index_1 ON table_1 (col_1, col_2 ... )` - 인덱스 생성

`DROP INDEX index_1`  - 스키마 객체인 경우 / `DROP INDEX index_1 ON table_1`  - 테이블 내 객체인 경우

참고

* EXPLAIN - 인덱스를 사용해 검색하는지 확인할때 사용

  EXPLAIN SELECT * FROM table_1 WHERE col_1 = 5;

<br>

예시)

* CREATE INDEX index_1 ON table_1 (col_1, col_2);
  SELECT * FROM table_1 WHERE col_1 = 2 AND col_2 = 4;  -  인덱스가 있는 열을 사용시 검색이 빨라짐
* DROP INDEX index_1 ON table_1

<br>

###  뷰

데이터베이스 객체로 등록할 수 없는 SELECT 명령을 객체로서 이름을 붙여 관리할 수 있도록 한 것

`CREATE VIEW view_1 AS SELECT 명령` 형태로 사용함 (뷰에 열 지정 가능, 뷰명 뒤에 괄호로 묶어 열을 나열함)

`DROP VIEW view_1` 형태로 사용함

저장공간을 사용하지 않지만, CPU 사용을 함

참고)

* 머티리얼라이즈드 뷰 (Materialized View)

  뷰는 데이터를 일시적으로 저장했다가 쿼리가 실행 종료될 때 함께 삭제가 되는데, 머티리얼라이즈드 뷰는 데이터를 일시적으로 저장해 사용하는 것이 아니라 테이블처럼 저장장치에 저장해두고 사용함 (CPU연산 사용량을 줄일 수 있음)

  단, 뷰에 지정된 테이블의 데이터가 변경되면 SELECT 명령을 재실행하여 데이터를 다시 저장함

<br>

예시)

* CREATE VIEW view_1 (ncol_1, ncol_2) AS SELECT col_1, col_2 FROM table_1;
  SELECT * FROM view_1 WHERE ncol_1 = 10;
* 

---

## 📖 참고

서적 - [SQL 첫걸음](https://book.naver.com/bookdb/book_detail.nhn?bid=9738902)