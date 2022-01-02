import sys


def chk(y, x):
    for i in range(1, y+1):         
        if x - i >= 0 and cols_selected[x] - i == cols_selected[x-i]:       # 현재 열의 행과 옆에 떨어진 열의 행이 같을때
           return False                                                     # 위로 올라갈수록 대각선에 퀸이 있을때
        elif x + i < N and cols_selected[x] - i == cols_selected[x+i]:
            return False
    return True

def solution(n):
    global answer

    if n >= N:              # 모든 행에 놓았으면 정답 개수 증가
        answer += 1
        return

    for c in range(N):
        if cols_selected[c] == -1:          # 열에 퀸이 놓여있지 않으면
            if chk(n, c):                   # 위에 행 중 대각선에 퀸이 없을때
                cols_selected[c] = n        # 지금 열에 행 번호 저장
                solution(n+1)               # 다음 행 탐색
                cols_selected[c] = -1

N = int(sys.stdin.readline())               # 체스판의 크기
cols_selected = [-1] * N                    # 열에 퀸이 놓였는지 유무 판별 및 몇번 행에 놓였는지 저장
answer = 0                                  # 정답을 저장할 변수

solution(0)                                 # 0번 행부터 시작

print(answer)                               # 출력