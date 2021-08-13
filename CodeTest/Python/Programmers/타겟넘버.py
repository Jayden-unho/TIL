def solution(numbers, target):
    answer = 0
    sum_numbers = sum(numbers)
    
    for i in range(1<<len(numbers)):            # 각 요소가 음수 아니면 양수이므로 2가지 경우의 수
        tmp_sum = sum_numbers                   # 리스트의 합을 임시변수에 저장
        for j in range(len(numbers)):
            if i & (1<<j):
                tmp_sum += (numbers[j] * -2)    # 임시변수에 각 요소가 음수인 경우 합산
        if tmp_sum == target:                   # 타겟변수와 값이 같으면 카운트
            answer += 1
    
    return answer