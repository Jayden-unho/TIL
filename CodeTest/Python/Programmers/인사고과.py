def solution(scores):
    sorted_scores = sorted(
        sorted(scores, key=lambda x: x[1]), reverse=True, key=lambda x: x[0])
    target = scores[0][:]
    answer = 1
    grade = {}

    max_score = 0
    for score in sorted_scores:
        a, b = score
        total = a + b

        if b < max_score:
            if target == score:
                return -1
            continue

        max_score = b
        grade[total] = grade.get(total, 0) + 1

    for k in sorted(grade.keys(), reverse=True):
        num = grade[k]
        if sum(target) == k:
            break
        answer += num

    return answer


print(solution([[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]]))
print(solution([[1, 1], [2, 2], [2, 2], [3, 3]]))
print(solution([[3, 4], [4, 1], [4, 3], [
      4, 2], [4, 4], [3, 1], [3, 2], [3, 2]]))
