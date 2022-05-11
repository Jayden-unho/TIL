def solution(n, s):
    answer = []
    num = s // n
    remain = s % n

    if not num:             # 합이 집합의 개수로 나누어지지 않는 경우
        return [-1]         # 배열 생성이 불가능하므로 -1 반환

    answer = [num] * n      # 정답 배열을 전부 몫으로 채움

    for i in range(remain): # 나머지 값만큼 반복하여 배열에 1씩 더한다
        answer[-i-1] += 1

    return answer

print(solution(2, 9))
print(solution(2, 1))
print(solution(2, 8))