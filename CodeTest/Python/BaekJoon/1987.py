import sys
sys.stdin = open('input.txt')

dr = [-1, 0, 1, 0]                                              # 위 오른쪽 아래 왼쪽
dc = [0, 1, 0, -1]

def solution():
    global answer

    s = set([(0, 0, board[0][0])])                              # 좌표, 지나온 좌표들의 알파벳 기록 (시간 단축을 위해 일반 리스트가 아닌 집합으로 관리)

    while s and answer < 26:                                    # 탐색할게 아직 남았거나, 알파벳 26개를 모두 찾은 경우 종료
        y, x, ans = s.pop()                                     # 좌표, 발견한 알파벳 기록

        for k in range(4):
            r = y + dr[k]                                       # 다음 좌표
            c = x + dc[k]       

            if 0 <= r < R and 0 <= c < C:
                if board[r][c] not in ans:                      # 현재 좌표의 알파벳이 이전에 지나오지 않았다면
                    s.add((r, c, ans + board[r][c]))            # 집합에 추가
                    answer = max(answer, len(ans)+1)            # 정답 최댓값 갱신

R, C = map(int, sys.stdin.readline().split())                       # 세로, 가로
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]     # 배열의 정보
answer = 1                                                          # 정답 (시작이 포함되어야 하므로 최소 1)

solution()                                                      # 탐색

print(answer)                                                       # 출력