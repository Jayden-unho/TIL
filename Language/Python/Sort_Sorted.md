## Sort() 와 Sorted()

#### 차이

* `list.sort()` 는 리스트를 제자리에서 수정하는 내장 메서드
  리스트에서만 사용가능
* `sorted(iterable)` 는 이터러블로부터 새로운 정렬된 리스트를 만듦
  리스트 외에 다른 이터러블을 받아서 정렬 가능



#### key 함수

* sort()와 sorted()는 모두 비교하기 전에 각 리스트 요소에 대해 호출할 함수(또는 다른 콜러블)를 지정하는 key 매개 변수를 가지고 있다.

아래의 예시를 보면 리스트에서 각 인덱스에 튜플로 저장이 되어있는데, 그 값에 접근하여 나이의 오름차순으로 정렬 할수있다.

```python
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```



아래 예시와 같이 인덱스 번호가 아닌 이름을 이용해서 접근 가능

```python
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
sorted(student_objects, key=lambda student: student.age)   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```



아래와 같이 다중 정렬 가능

```python
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

sorted(student_tuples, key=lambda student: (student[1], student[2]))   # sort by age
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12), ]
```



하나는 오름차순으로 정렬하고, 다음으로 다른 하나는 내림차순을 원하는 경우

1.  두번째 사항을 내림차순을 진행
2. 첫번째 사항을 오름차순으로 다시 정렬

```python
s = sorted(student_objects, key=attrgetter('age'))     # sort on secondary key
sorted(s, key=attrgetter('grade'), reverse=True)       # now sort on primary key, descending

[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```





#### operator 모듈 함수

파이썬은 액세스 함수를 더 쉽고 빠르게 만드는 편리한 함수 제공

operator 모듈에는 itemgetter(), attrgetter() 및 methodcaller() 함수가 있음



```python
from operator import itemgetter, attrgetter
sorted(student_tuples, key=itemgetter(2))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

sorted(student_objects, key=attrgetter('age'))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

