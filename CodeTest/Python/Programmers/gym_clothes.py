def solution(n, lost, reserve):
    answer = 0
    student = [1 for _ in range(n)]
    
    for idx in lost:
        student[idx-1] -= 1
    
    for idx in reserve:
        student[idx-1] += 1

    for idx in range(1, len(student)):
        if student[idx] == 2 and student[idx-1] == 0:
            student[idx] -= 1
            student[idx-1] += 1
        elif student[idx] == 0 and student[idx-1] == 2:
            student[idx] += 1
            student[idx-1] -= 1

    for e in student:
        if e:
            answer += 1

    return answer
    


print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(3, [3], [1]))