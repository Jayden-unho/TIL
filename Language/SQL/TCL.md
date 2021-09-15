[[_TOC_]]

<br>

# SQL_TCL (Transaction Control Language)

## 트랜잭션 (Transaction)

여러 단계로 처리를 나누어 SQL 명령을 실행하는 경우에 트랜잭션을 자주 사용함

트랜잭션을 사용해서 데이터를 추가한다면 에러가 발생해도 트랜잭션을 롤백해서 종료할 수 있음

롤백하면 트랜잭션 내에서 행해진 모든 변경사항을 없었던 것으로 할 수 있고, 아무런 에러 발생하지 않는다면 변경사항을 적용하고(커밋) 트랜잭션을 종료함



커밋 (COMMIT) - 쿼리를 실행하고 에러가 없을 경우 커밋을 사용하여 실행된 쿼리를 적용시킴

롤백 (ROLLBACK) - 쿼리를 실행하고 에러가 발생하는 경우 롤백을 사용하여 실행한 쿼리를 모두 취소시킴



MySQL - START TRANSACTION 명령 사용

SQL Server, PostgreSQL - BEGIN TRANSACTION 명령 사용

Oracle, DB2 - 트랜잭션을 시작하는 명령 따로 없음 (자동 커밋이 아님)



예시)

* START TRANSACTION

  SELECT * FROM table_1;

  INSERT INTO table_1 VALUES ('1', 0);

  COMMIT;  /  ROLLBACK;