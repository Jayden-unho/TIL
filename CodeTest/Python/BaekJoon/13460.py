import sys
sys.stdin = open('input.txt')

dr = [-1, 0, 1, 0]                              # 위 오른쪽 아래 왼쪽
dc = [0, 1, 0, -1]

def solution(ans, blue, red, direction):        # 기울인 횟수, 파란공의 좌표, 빨간공 좌표, 기울인 방향
    global answer

    if ans > 10:                                # 10번 넘게 기울인 경우 탐색 중지
        return
    elif answer <= ans:                         # 이미 구한 정답 횟수보다 더 많이 기울이면 탐색 종료
        return

    red = move(red, blue, direction)            # 빨간공 이동
    blue = move(blue, red, direction)           # 파란공 이동
    if board[red[0]][red[1]] != 'O':            # 빨간공이 구멍에 빠진것이 아니면, 한번 더 이동
        red = move(red, blue, direction)        # 빨간공이 진행할 방향 바로 앞에 파란공이 있으면, 파란공으로 인해 진행을 못하기에
                                                # 빨간공 -> 파란공 -> 빨간공을 진행시켜야 함

    end = is_end(red, blue)                     # 빨간공과 파란공이 구멍에 빠졌는지 확인
    if not end:                                 # 어느 공도 구멍에 빠지지 않았으면
        for k in range(4):                      # 4개의 방향으로 기울여서 탐색
            solution(ans+1, blue, red, k)
    else:
        if end == 'win':                        # 빨간공만 빠진 경우, 현재까지 기울인 횟수 저장
            answer = ans
    
def move(ball, other_ball, direction):          # 공을 이동시키는 함수
    y, x = ball                                 # 이동 시킬 공의 좌표

    while True:
        r = y + dr[direction]                   # 다음 좌표
        c = x + dc[direction]

        if board[r][c] == '.':                  # 다음 좌표가 비어있는데
            if (r, c) == other_ball:            # 다른 색 공이 있다면, 현재 좌표 그냥 반환
                return (y, x)
            else:                               # 다른 색 공이 없다면, 한칸 이동
                y, x = r, c
        elif board[r][c] == '#':                # 다음 좌표가 벽이라면, 현재 좌표 반환
            return (y, x)
        elif board[r][c] == 'O':                # 다음 좌표가 구멍이라면, 구멍의 좌표 반환
            return (r, c)

def is_end(red, blue):                                      # 공 두개 중 하나라도 구멍에 빠졌는지 확인
    ry, rx = red
    by, bx = blue

    if board[ry][rx] != 'O' and board[by][bx] != 'O':       # 두개다 아직 안빠졌으면
        return False
    elif board[ry][rx] == 'O' and board[by][bx] != 'O':     # 빨간공만 빠졌으면
        return 'win'
    elif board[ry][rx] != 'O' and board[by][bx] == 'O':     # 파란공만 빠졌으면
        return 'lose'   
    elif board[ry][rx] == 'O' and board[by][bx] == 'O':     # 둘다 빠졌으면
        return 'lose'


N, M = map(int, sys.stdin.readline().split())                       # 행, 열 길이
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]     # 보드판
answer = 1e10                                                       # 최초 정답 초기화

for i in range(N):                                  # 보드판 반복하여
    for j in range(M):                              # 빨간공과 파란공 위치 탐색
        if board[i][j] == 'B':
            board[i][j] = '.'
            blue = (i, j)
        elif board[i][j] == 'R':
            board[i][j] = '.'
            red = (i, j)

for k in range(4):                                  # 4방향으로 기울여가며 탐색 시작
    solution(1, blue, red, k)

print(-1) if answer == 1e10 else print(answer)      # 10번 이하로 못 찾았으면 -1 출력, 그 외에 정답 출력