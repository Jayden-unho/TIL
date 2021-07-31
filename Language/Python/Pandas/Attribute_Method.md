# Attribute_Method

## Index

* **Attribute**
* **Method**

  

---

### Attribute

##### .dtypes

- 각 열의 이름과 데이터 형식을 나란히 표시할 수 있음

 

##### .index

- 인덱스 길이를 표시할 수 있음



##### .size

- 길이를 알 수 있음





---

### Method

##### value_counts()

-  각 데이터의 개수를 반환한다.
- 안의 파라미터로 normalize=True 로 설정시 개수 대신 상대 빈도 값이 반환 됨



##### info()

- 시리즈처럼 각 열별 이름, 데이터 갯수(null이 아닌 값의 갯수), 데이터 타입과 같은 정보 반환, DataFrame에서 사용된 메모리 크기가 나열됨



##### apply()

- 파이썬에서 map() 과 유사한 메서드



##### unique()

- 중복 제거, 파이썬의 set과 유사



##### sample(n=5, random_state=42)

- 데이터 중 일부를 가져올 수 있음, 위의 경우 랜덤으로 가져옴



##### count()

- size, shape, len() 과 다르게 count는 결측치를 제외한 아이템의 개수를 반환
  전자의 3개는 결측치도 포함한 모든 아이템의 개수를 반환



##### min()

- 최소값



##### max()

- 최댓값



##### mean()

- 평균값



##### median()

- 중간값



##### std()

- 표준편차



##### describe()

- 요약 통계량과 몇가지 분위스를 표시할 수 있음
- 숫자 데이터 열과 문자열 데이터 열의 결과는 다르게 나타난다



##### quantile()

- 수치 데이터의 분위수를 계산함



##### hasnans()

- 시리즈에서 결측치의 존재 여부를 알 수 있음 (불린 단일값 반환)



##### isna() or isnull()

- 각 개별값의 결측치 여부를 알 수 있음 (True - 결측치, False - 정상) (시리즈 형태로 반환)



##### notna()

- 결측치가 아닌 모든 값에 대해 True 반환 (isna 메서드와 반대 됨)



##### fillna(0)

- 시리즈 내의 결측치 값을 변경 가능 위의 경우 0으로 대체



##### dropna()

- 결측치 제거



##### add(), sub(), mul(), div(), floordiv(), mod(), pow(), lt(), gt(), le(), ge(), eq(), ne()

- 현재 시리즈에서 파라미터 값을 연산한다. (시리즈 내의 모든 데이터에 동일하게 연산)
- 단순 연산자 이용시 결측치가 무시 됨
- 파라미터로 fill_value=? 을 이용해 결측치에 ? 값을 채워 연산 가능



##### astype()

- 파라미터 값으로 타입 입력시 해당 타입으로 타입 변환
- 단, 시리즈 내에 결측치가 없어야 함, 따라서 결측치를 0으로 바꾸고 int 형으로 바꿈



##### pipe()

- 메서드 체인 중간에 출력을 하고 싶을때 pipe() 파라미터로 함수를 전달하여 중간 과정의 값 출력 가능

- ```python
  # 사용 예시
  # 중간에 전역변수에 값을 넣고 싶을때도 응용 가능함
  global_var = None
  
  def debug(ser):
    global global_var
    global_var = ser
    
    print("before")
    print(ser)
    print("after")
    return ser
  
  Series.fillna(0).pipe(debug).astype(int).head()
  ```



##### rename()

- 열 이름을 변경 가능하다.

- 파라미터 값으로 딕셔너리를 전달한다.

- ```python
  # example
  col_map{
    "old1" : "new1",
    "old2" : "new2",
  }
  
  DataFrame.rename(columns=col_map)
  ```

- 파라미터에 함수 전달 가능 

- ```python
  #example
  def to_clean(val):
    return val.strip().lower().replace(' ', '_')
  
  DataFrame.rename(columns=to_clean)
  ```

* 위의 경우와 흡사하게 함수대신 리스트 컴프리핸션도 사용 가능



##### assign()

- 새 열이 추가된 새로운 DataFrame 을 반환한다.
- 파라미터로 열이름=0 혹은 열이름='' 방식으로 사용



##### insert()

- 데이터프레임 특정 위치에 새 열을 삽입할 수 있음
- 파라미터로 세개를 필요로 함 (새 열의 인덱스 위치, 새 열의 이름, 값)
- 새로운 데이터프레임 반환이 아니라 None을 반환



##### drop()

- 행이나 열 삭제
- 파라미터로 columns='열 이름' 입력하면 해당 열을 삭제한다
- 파라미터로 axis 입력하여 행을 삭제할지 열을 삭제할지 넣는다, 기본 0