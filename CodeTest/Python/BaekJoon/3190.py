import sys
from collections import deque
sys.stdin = open('input.txt')


def solution():
    snake = deque([(1, 1)])             # 뱀의 몸이 있는 위치
    direction = 1                       # 뱀의 진행 방향
    com_idx = 0                         # 방향 전환하는 정보의 인덱스
    time = 0                            # 흐른 시간

    while True:
        time += 1                       # 1초 증가

        head = snake.popleft()          # 뱀의 머리 부분
        r = head[0] + dr[direction]     # 뱀의 머리가 이동할 다음 좌표
        c = head[1] + dc[direction]

        if r < 1 or r >= N+1 or c < 1 or c >= N+1 or (r, c) in snake:       # 벽에 부딪히거나 본인 몸에 부딪히면 종료
            return time 
        else:                               # 정상적으로 움직이면
            snake.appendleft(head)          # 뱀의 원래 머리 위치와 다음 위치 추가
            snake.appendleft((r, c))
            tail = snake.pop()              # 앞으로 이동하므로 꼬리 부분 제거

            if (r, c) in apple:             # 그러나 사과를 먹은 경우, 몸의 길이 증가로
                snake.append(tail)          # 꼬리부분 다시 추가
                apple.remove((r, c))        # 사과는 한번 먹으면 사라지게 설정

        if com_idx < len(command) and command[com_idx][0] == time:      # 방향 전환할 시간이라면
            if command[com_idx][1] == 'D':          # 오른쪽 방향으로
                direction = (direction+1) % 4
            elif command[com_idx][1] == 'L':        # 왼쪽 방향으로
                direction = (direction-1) % 4
            com_idx += 1                            # 인덱스 증가
        

dr = [-1, 0, 1, 0]                  # 상 우 하 좌
dc = [0, 1, 0 ,-1]

N = int(sys.stdin.readline())       # 보드의 크기
K = int(sys.stdin.readline())       # 사과의 개수
apple = {tuple(map(int, sys.stdin.readline().split())) for _ in range(K)}       # 사과 위치 값

L = int(sys.stdin.readline())       # 뱀의 방향 전환 횟수
command = [tuple(map(lambda x: int(x) if x.isdigit() else x, sys.stdin.readline().split())) for _ in range(L)]      # 방향 전환 정보

print(solution())       # 탐색