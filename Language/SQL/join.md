[[_TOC_]]

<br>

# SQL 테이블 결합 (JOIN)

외부키(FOREIGN KEY) - 다른 테이블의 기본키를 참조하는 열을 외부키(FOREIGN KEY)라고 한다

테이블 결합시 어느쪽이 하나의 행인지, 여러 행인지 (1:N, N:1, N:N) 의 경우가 있다.

<br>

## 교차 결합 (CROSS JOIN)

`SELECT * FROM table_1, table_2...;` 형태로 사용

교차결합을 사용시 곱집합으로 계산함

열은 table_1, table_2 의 열 수를 합치고, 행은 table_1 의 col_1 의 갯수 * table_2 의 col_2 의 갯수 한 결과값이 된다.

교차 결합 사용시 테이블 수가 많아지면 조합의 수가 엄청나게 늘어나서 집합이 거대해져, 많은 테이블을 교차결합하는 경우는 드물다.

<br>

## 내부 결합

하나의 테이블에 너무 많고 다양한 데이터를 담아지면 동일한 데이터가 중복해서 여러곳에 저장되는 경우가 있다.

만약 데이터 변경시 이곳저곳에 저장된 데이터를 모두 수정하기에는 까다로움.

따라서 데이터들의 특징을 파악하여 여러 테이블로 나누고, 필요시에 다른 테이블을 참조하여 데이터를 확인한다.

테이블에는 하나의 기본키(PRIMARY KEY)가 존재하여 이러한 기본키로 다른 테이블을 참조하는데 활용



### INNER JOIN

`FROM table_1 INNER JOIN table_2 ON table_1.col_1 = table_2.col_1` 와 같은 형태로 사용

예시)

* SELECT table_1.col_1, table_2.col_2 FROM table_1 INNER JOIN table_2 ON table_1.col_3 = table_2.col_3;

<br>

## 외부 결합

어느 한쪽에만 존재하는 데이터행을 어떻게 다룰지를 변경할 수 있는 결합 방법

하나의 테이블에 새로운 데이터가 추가되고 나머지 하나는 이를 인식하지 못한다면, 내부 결합 사용시 새롭게 추가된 데이터는 제외된다.

외부 결합은 결합하는 테이블 중에 어느쪽을 기준으로 할지 결정할 수 있음



### LEFT JOIN, RIGHT JOIN

결합의 어느쪽을 기준으로 하느냐의 차이

예시)

* SELECT table_1.col_1, table_2.col_2 FROM table_1 LEFT JOIN table_2 ON table_1.col_3 = table_1.col_3;

