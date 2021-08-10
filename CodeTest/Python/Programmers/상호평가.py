'''
1. 학생들 각 개인의 점수가 담기게끔 리스트를 전치시킨다.
2. for 문으로 반복
3. 리스트 내 max, min, 구하고 본인이 준 점수와 일치하면 유일한 점수인지 판별
4. 유일한 점수이면 remove

* 새로운 학습 내용 *
zip 함수를 사용하면 결합된 리터러블이 기본적으로 튜플 형태로 반환이 된다.
만약 리스트 하나하나를 리스트 형태로 받고 싶다면 map 함수를 이용하면 된다.

* 예상 시간 복잡도 - O(N^2)
학생들 반복 for - O(N)
    max - O(N)
    min - O(N)
    count - O(N)
    remove - O(N)
    len - O(N)
'''

def solution(scores):
    avg = []                                                    # 평균을 담을 리스트 변수
    answer = ''                                                 # 정답을 저장할 변수
    individual_score = list(map(list, zip(*scores)))            # zip 함수를 이용하여 개인의 점수들을 리스트로 만듦

    for idx in range(len(individual_score)):                    # 학생 개인의 점수 리스트에 인덱스로 접근
        self_score = individual_score[idx][idx]                 # 본인이 준 점수
        max_value = max(individual_score[idx])                  # 본인이 받은 최고 점수
        min_value = min(individual_score[idx])                  # 본인이 받은 최저 점수
        
        if (self_score == max_value or self_score == min_value) and individual_score[idx].count(self_score) == 1:   # 본인이 준 점수가 최저이거나 최고일때, 그게 유일한 점수라면
            individual_score[idx].remove(self_score)            # 본인이 준 점수 삭제
        
        avg.append(sum(individual_score[idx]) / len(individual_score[idx]))     # 평균 구함
    
    for e in avg:                                               # 학점 등급을 나눈다
        if e >= 90:
            grade = 'A'
        elif e >= 80:
            grade = 'B'
        elif e >= 70:
            grade = 'C'
        elif e >= 50:
            grade = 'D'
        else:
            grade = 'F'

        answer += grade        

    return answer


print(solution([[100,90,98,88,65], [50,45,99,85,77], [47,88,95,80,67], [61,57,100,80,65], [24,90,94,75,65]]))
print(solution([[50,90],[50,87]]))
print(solution([[70,49,90],[68,50,38],[73,31,100]]))