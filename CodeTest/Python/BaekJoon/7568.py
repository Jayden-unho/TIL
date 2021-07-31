# 풀이1
import sys

people = int(sys.stdin.readline().rstrip())
people_data = []

# 사람들의 데이터를 입력받아서 리스트 형태로 정리함
for _ in range(people):
    people_data.append(list(map(int, sys.stdin.readline().split())))

# 자신을 포함한 모든 경우의 수를 탐색
for i in range(people):
    grade = 1
    for j in range(people):
        tall = people_data[i][0] - people_data[j][0]
        weight = people_data[i][1] - people_data[j][1]

        # 본인보다 키와 몸무게가 모두 큰 경우에 등수를 하나씩 밀린다
        if tall < 0 and weight < 0:
            grade += 1
    people_data[i].append(grade)

for g in people_data:
    print(g[2])

# 풀이2
'''
import sys

n = int(sys.stdin.readline())
people = []

# 사람들 데이터를 받으면서 각자의 등수를 1등으로 설정해둠
for i in range(n):
    people.append(list(map(int, sys.stdin.readline().split())))
    people[i].append(1)

# 두 대상을 한번씩만 비교 위와 다르게 반복횟수가 적음
for i in range(n-1):
    for j in range(i, n):
        tall = people[i][0] - people[j][0]
        weight = people[i][1] - people[j][1]

        # 앞사람이 키와 몸무게 모두 클 경우, 뒷사람 등수를 올림
        if tall > 0 and weight > 0:
            people[j][2] += 1
        # 뒷사람이 키와 몸무게 모두 클 경우, 앞사람 등수를 올림
        elif tall < 0 and weight < 0:
            people[i][2] += 1

for k in range(n):
    print(people[k][2], end=' ')
'''