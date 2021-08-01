def solution(lottos, win_nums):
    LOTTO_RANK = [6, 6, 5, 4, 3, 2, 1]
    
    answer = []
    zero_cnt = 0
    right_num_cnt = 0

    for lotto in lottos:
        if not lotto:
            zero_cnt += 1
        elif lotto in win_nums:
            right_num_cnt += 1
    
    answer.append(LOTTO_RANK[zero_cnt+right_num_cnt])
    answer.append(LOTTO_RANK[right_num_cnt])    

    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))