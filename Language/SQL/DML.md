

[[_TOC_]]

<br>

---

# SQL_DML (Data Manipulation Language)

## 명령어

### FROM

데이터 조회, 수정 등 명령어 실행시 해당 명령어를 수행할 테이블을 지정함

`FROM 테이블명` 형식으로 사용함 

위치 - SELECT, INSERT, DELETE, UPDATE 구 뒤에 나타남

<br>

예시)

- SELECT * FROM table_1;

<br>

### WHERE

조건을 지정하는 구 (행)

`WHERE 조건1 AND 조건2` 형식으로 사용함

위치 - FROM 구 뒤에 위치함

연산자 종류

* =

  같다

* <>

  같지 않다

* \>

  작다

* <

  크다

* \>=

  작거나 같다

* <=

  크거나 같다

* IS NULL

  NULL 값

* IS NOT NULL

  NULL 값이 아니다

* AND

  2개의 조건이 모두 참인 경우

* OR

  2개 중 하나의 조건만 참이여도 됨

* NOT

  해당 하는 조건이 아닌 경우

패턴 매칭

- LIKE 술어 사용
- `열명 LIKE 패턴` 형식으로 사용
- 메타문자 : % - 임의의 문자열, _ - 임의의 문자 하나
- 예시) SELECT * FROM table_1 WHERE col_1 LIKE %연습_;
  col_1 열에서 '연습'이라는 단어 앞에는 임의의 문자열이 들어오고 바로 뒤에는 임의의 한글자만 있는 경우만 조건에 부합함

참고

- 연월일을 하이픈(-) 으로 구분, 시각은 시분초를 클론(:) 으로 구분하여 표기

<br>

예시)

- SELECT * FROM table_1 WHERE col_1 = 3;
- SELECT * FROM table_1 WHERE col_1 = 3 AND col_2 = '이름';

<br>

### ORDER BY

데이터를 조회할때 행 순서를 정렬하여 볼 수 있음

`ORDER BY 열명 [정렬방식]` 형태로 사용 됨

위치 - WHERE 구 뒤에 위치함

정렬방식의 종류

- ASC - 오름차순 (기본 설정으로 생략 가능)
- DESC - 내림차순
- 참고 - 숫자는 숫자의 대소관계로 정렬, 문자는 알파벳 < 한글 (자음 < 모음) 순서(사전식)로 오름차순이다

<br>

예시)

- SELECT * FROM table_1 WHERE col_1 = 1 ORDER BY col_1;
- SELECT * FROM table_1 WHERE col_1 = 1 ORDER BY col_2 DESC;
- SELECT * FROM table_1 WHERE col_1 = 1 ORDER BY col_1 ASC, col_2 DESC;

<br>

### LIMIT

조회되는 행의 갯수를 제한하는데 이용

`MySQL` 과 `PostgreSQL` 에서만 사용 가능 / `SQL Server` 에서는 `TOP` / `Oracle` 에서는 `ROWNUM`

`LIMIT 행수 [OFFSET 시작행]` 형태로 사용 / offset 은 앞에 몇개의 행을 건너 뜀을 의미

위치 - SELECT 명령 마지막에 위치하여 WHERE 나 ORDER BY 뒤에 위치함

<br>

예시)

- SELECT * FROM table_1 LIMIT 3;
- SELECT * FROM table_1 LIMIT 3 OFFSET 3;

<br>

### CASE

CASE 를 이용하여 데이터 변환을 할 수 있음 (특정 값을 다른 값으로 변경하거나 NULL 값을 0으로 변환하는데 이용)

SELECT, WHERE, ORDER BY 등 에서 사용 가능

ELSE 생략시 ELSE NULL 이 됨

검색CASE 와 단순CASE 로 나뉨

#### 검색 CASE

`CASE WHEN 조건식1 THEN 식1 [WHEN 조건식2 THEN 식2] [ELSE 식3] END` 형태로 사용

<br>

예시)

* SELECT col_1, CASE WHEN col_1 IS NULL THEN 0 ELSE col_1 END AS "col_1(null=0)" FROM table_1;

  col_1 열에서 NULL 값은 0으로 바꾸고, NULL 이 아닌값은 기존값을 유지한다. 새로운 열의 이름은 col_1(null=0) 이 된다.

<br>

#### 단순 CASE

`CASE 식1 WHEN 식2 THEN 식3 [WHEN 식4 THEN 식5] [ELSE 식6] END` 형태로 사용

<br>

예시)

* SELECT col_1, CASE col_1 WHEN IS NULL THEN 0 ELSE col_1 END AS "col_1(null=0)" FROM table_1;

### SELECT

테이블에서 데이터를 조회할때 사용, 열을 지정해서 원하는 열만 조회할 수 있다.

`SELECT 열이름, 열이름` 형태로 사용

 위치 - 문장의 맨 앞에 위치함

<br>

예시)

* SELECT * FROM table_1;
* SELECT col_1 FROM table_1;
* SELECT col_2, col_1, col_3 FROM table_1;

<br>

<br>

---

## 연산

열의 값들을 연산하여 새로운 열을 만들어 내거나, 조건을 만들어 낼 수 있다.

NULL 값은 어떤 연산을 하더라도 NULL 이 반환된다.

<br>

연산자 종류

- \+, -, *, /, %

  <br>

명령어와 함께 사용

- SELECT

  연산한 결과가 새로운 열로 생성된다.

  열 이름은 연산 내용이 열이름이 된다. 단, AS 를 사용하여 별명을 지정할 수 있다.

  별명을 한글로 사용하는 경우에는 더블쿼트("")로 둘러싼다, 영어와 숫자는 있어도 되고 없어도 상관 없음

  

  예시)

  * SELECT col_1, col_1 * col_2 FROM table_1;
  * SELECT *, col_1 + col_2 AS "result" FROM table_1;

  <br>

- WHERE

  조건에서 연산하여 연산결과의 조건에 해당하는 행을 반환함

  WHERE 조건에서 SELECT 에서 지정한 별명을 사용할 수 없음 -> 코드 실행이 WHERE 가 먼저 실행되고 SELECT 가 실행되어 WHERE 에서는 별명이 아직 지정된 상태가 아니므로

  


  예시)

  * SELECT * FROM table_1 WHERE col_1 * col_2 >= 2000;

  <br>

- ORDER BY

  ORDER BY 는 가장 마지막에 실행되므로 SELECT 에서 지정한 별명을 사용하여 정렬 가능

  

  예시)

  * SELECT * FROM table_1 ORDER BY col_1 * col_2 DESC;
  * SELECT *, col_1 * col_2 AS "result" FROM table_1 ORDER BY result;

<br>

### 문자열 연산

문자열 결합 - \+ (SQL Server), || (Oracle, DB2, PostgreSQL), CONCAT(a, b) (MySQL)

문자열 추출 - SUBSTRING(string, start_idx, end_idx) - 기존에 아는 인덱스와 조금 다르므로 인덱스 주의!

함수

* TRIM(string)

  문자열 앞뒤로 여분의 스페이스가 있을 경우 이를 제거해줌

* CHARACTER_LENGTH(string)

  문자열의 길이를 반환해주는 함수

* OCTET_LENGTH(string)

  문자열의 길이를 바이트 단위로 계산해서 돌려주는 함수

<br>

### 날짜 연산

날짜와 시간 데이터를 저장하는 방법은 데이터베이스 제품에 따라 크게 다름

날짜시간 데이터를 연산하면 결과로 동일한 날짜시간 유형의 데이터를 반환하는 경우도 있으며 기간(간격)의 차를 나타내는 기간형 데이터를 반환하는 경우도 있음

명령어

* CURRENT_TIMESTAMP

  시스템 날짜를 확인할 수 있음, FROM 생략 가능, Oracle 에서는 생략 불가

  예시) SELECT CURRENT_TIMESTAMP;

  <br>

* TO_DATE('날짜', '서식'), TO_CHAR()

  Oracle 에서만 해당

  날짜 데이터의 서식을 임의로 지정, 변환할 수 있는 함수 - TO_DATE

  날짜형 데이터를 서식에 맞춰 변환해 문자열 데이터로 출력하는 함수 - TO_CHAR

  예시) TO_DATE('2014/10/23', 'YYYY/MM/DD')

  <br>

* CURRENT_DATE INTERVAL

  시스템 날짜의 며칠 전/후 를 계산할때 사용

  예시) SELECT CURRENT_DATE + INTERVAL 1 DAY

  <br>

  <br>

---

## 함수

종류

* MOD(a, b)

  a/b 연산의 나머지 값을 반환

* ROUND(a, [,b])

  소수 a 를 반올림한 값을 반환

  소수 뒤에 정수를 넣어 몇번째 자리에서 반올림할지 정할 수 있음 (기본값 0 - 소수 첫번째 자리에서 반올림 ex) 3.67 -> 4)

* TRUNCATE(a, [,b])

  소수 a 자릿수 버림

* COALESCE(col_1, 0)

  NULL 값을 변경하는데 사용되는 함수

  인자로 열이름, 변경될 값 이 들어간다.