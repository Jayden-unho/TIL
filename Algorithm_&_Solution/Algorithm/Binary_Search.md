# Binary Search (이진 탐색)

## 개념

데이터가 정렬되어 있는 배열에서 특정 값을 찾아내는 알고리즘이다. 배열의 중간에 있는 값을 선택하여 찾고자 하는 값과 현재 선택된 값을 비교하여 현재 값이 더 작으면 오른쪽 데이터에서 탐색하고, 현재 값이 더 크면 왼쪽 데이터를 탐색하여 해당 값을 찾게 된다.



## 로직

![Binary_Search01](../../Image.assets/Algorithm_&_Solution/Algorithm/Binary_Search01.png)

 

## 시간복잡도

* O(log n)



## 구현

* 일반적인 함수

```python
# 이진 탐색 함수
def binary_search(in_list, target):
    low = 0
    high = len(in_list)
    
    # low 값이 high 값을 넘어가버리면 종료
    while low <= high:
        # 탐색을 위해 가운데 값 설정
        mid = (low+high)//2
        
        # 찾으려는 값보다 큰 경우, 왼쪽 부분 탐색
        if in_list[mid] > target:
            high = mid - 1
        # 찾으려는 값보다 작은 경우, 오른쪽 부분 탐색
        elif in_list[mid] < target:
            low = mid + 1
        # 값을 찾았을 경우
        else:
            return mid
    
    return '찾으려는 값이 없습니다.'
```



* 재귀 함수

```python
def binary_search_recursive(in_list, target, low, high):
    if low > high:
        return '찾으려는 값이 없습니다.'
    
    mid = (low+high)//2
    
    if in_list[mid] > target:
        binary_search_recursive(in_list, target, low, mid-1)
    elif in_list[mid] < target:
        binary_search_recursive(in_list, target, mid+1, high)
    else:
        return mid
```



* 파이썬 이진 탐색 모듈

```python
import bisect


in_list = [1,2,3,4,5,6,7,8,9,10]
# list에서 4를 찾아라
bisect.bisect(in_list, 4) # low, high 값은 키워드인자로 기본 설정값이 있음
```

[bisect 공식 문서](https://docs.python.org/ko/3.6/library/bisect.html)

