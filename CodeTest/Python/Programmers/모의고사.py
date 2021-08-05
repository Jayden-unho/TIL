ONE = [1, 2, 3, 4, 5]
TWO = [2, 1, 2, 3, 2, 4, 2, 5]
THREE = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

def solution(answers):
    count = [0, 0, 0]
    answer = []

    for idx in range(len(answers)):
        if answers[idx] == ONE[idx%5]:
            count[0] += 1
        if answers[idx] == TWO[idx%8]:
            count[1] += 1
        if answers[idx] == THREE[idx%10]:
            count[2] += 1

    max_num = max(count)

    for i in range(len(count)):
        if count[i] == max_num:
            answer.append(i+1)
    
    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))