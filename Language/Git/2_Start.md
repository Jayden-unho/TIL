# Git 시작하기

#### 깃허브와 이름, 이메일 설정

* 컴퓨터 전체

```git
git config --global user.name unho
git config --global user.email djsgh94@naver.com
```

* 폴더에만

```git
git config --local user.name unho
git config --local user.email djsgh94@naver.com
```



#### Git remote add origin 'http주소'

원격저장소에 origin이라 하는 별명으로 해당 주소에 등록함을 의미

원격 저장소에 최초 등록할때 사용함

clone과는 조금 다른 개념



#### 깃허브 Repositories 연동

1. 터미널(프롬프트)로 작업할 폴더로 들어간다.

2. 깃허브에서 연동할 Repositories에서 Clone HTTPS 주소를 복사한다.

3. 터미널에서 입력

4. ```git
   git clone 주소
   ```

5. 연동된 폴더에 들어가서 작업 시작
