import sys
sys.setrecursionlimit(100000000)
sys.stdin = open('input.txt')


def sol(s, min_length, cur_length):
    """
    현재 문자열이 목표하는 문자열이랑 일치하는지 탐색
    일치하지 않는다면 재귀적으로 탐색

    @params
    - s : 현재 문자열
    - min_length : 목표 문자열의 길이
    - cur_length : 현재 문자열의 길이
    """
    global answer

    if s == S:
        return 1
    elif cur_length <= min_length:
        return 0

    last_chr = s[-1]
    if last_chr == 'A':  # 가장 마지막 문자가 'A' 라면
        return sol(s[:-1], min_length, cur_length-1)
    else:  # 가장 마지막 문자가 'B' 라면
        return sol(s[:-1][::-1], min_length, cur_length-1)


S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

answer = sol(T, len(S), len(T))

print(answer)
