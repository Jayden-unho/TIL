# 데이터 프레임에서 여러 columns (Series) 를 연산 후 데이터 프레임에 새로운 열로 추가하는 방법

```python
#1. 단순히 연산자를 사용
total = (
	movies["one"]
  + movies["two"]
  + movies["three"]
)

# total_columns 라는 새로운 열 추가
movies.assign(total_columns=total)

# 단순 연산 이용시 결측치가 있으면 결과가 NaN 이 된다
```



```python
#2. 메서드 이용
cols = [
  'one',
  'two',
  'three',
]

sum_cols = movies.loc[:, cols].sum(axis=1)
movies.assign(total_columns=sum_cols)

# 결측치가 있어도 sum 메서드는 결측치를 무시함
```

