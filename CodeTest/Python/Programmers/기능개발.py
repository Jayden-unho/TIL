import math

def solution(progresses, speeds):
    answer = []
    remain = list(map(lambda x: math.ceil((100-x[0])/x[1]), zip(progresses, speeds)))
    
    remain.reverse()

    while remain:
        start_func = remain.pop()
        cnt = 1

        # 뒤에가 더 빨리 끝났으면
        while remain and start_func >= remain[-1]:
            remain.pop()
            cnt += 1

        answer.append(cnt)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))