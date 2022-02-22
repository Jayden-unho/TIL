# def solution(stones, k):
#     answer = 1e10

#     for idx in range(len(stones)-k+1):
#         can_move = max(stones[idx:idx+k])
#         answer = min(answer, can_move)

#     return answer

def solution(stones, k):
    low, high = 0, max(stones)
    answer = 0

    while low <= high:
        can = (low+high) // 2
        cnt = 0
        print(can, stones)

        for idx in range(len(stones)):
            if stones[idx] < can:
                cnt += 1
                if cnt >= k:
                    break
            else:
                cnt = 0
        
        if cnt >= k:
            high = can - 1
        else:
            low = can + 1
            answer = can
            
    return answer

            

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))