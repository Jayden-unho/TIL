def solution(d, budget):
    answer = 0
    
    for supply in sorted(d):
        if budget >= supply:
            budget -= supply
            answer += 1
    
    return answer


print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))