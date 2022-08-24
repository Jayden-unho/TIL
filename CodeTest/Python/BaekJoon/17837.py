import sys
sys.stdin = open('input.txt')


def get_pieces(num: int, y: int, x: int) -> list[int]:
    '''
    이동하는 말과 해당 말의 위에 올려진 말들 목록 반환
        params:
            num: 이동하는 말의 번호
            y: 행 좌표
            x: 열 좌표
    '''
    idx = piece[y][x].index(num)
    result = piece[y][x][idx:]
    piece[y][x] = piece[y][x][:idx]
    return result


def move_to_white(pieces: list[int], y: int, x: int) -> None:
    '''
    다음 좌표의 색상이 흰색인 경우, 말 이동
        params:
            pieces: 이동되는 말의 목록
            y: 이동하는 행 좌표
            x: 이동하는 열 좌표
    '''
    piece[y][x].extend(pieces)
    change_status(y, x, pieces)


def move_to_red(pieces: list[int], y: int, x: int) -> None:
    '''
    다음 좌표의 색상이 빨간색인 경우, 말 이동
        params:
            pieces: 이동되는 말의 목록
            y: 이동하는 행 좌표
            x: 이동하는 열 좌표
    '''
    pieces = pieces[::-1]   # 말 순서 뒤집기
    piece[y][x].extend(pieces)
    change_status(y, x, pieces)


def move_to_blue(pieces: list[int], y: int, x: int, num: int, direction: int) -> tuple[int, int]:
    '''
    다음 좌표의 색상이 파란색인 경우, 말 이동
        params:
            pieces: 이동되는 말의 목록
            y: 이동하는 행 좌표
            x: 이동하는 열 좌표
            num: 이동하는 말의 번호
            direction: 해당 말의 이동 방향
        returns:
            y: 최종적으로 이동한 행 좌표
            x: 최종적으로 이동한 열 좌표
    '''
    if 0 <= y < N and 0 <= x < N and board[y][x] != 2:  # 새로운 칸이 파란색이 아닐때
        if board[y][x] == 1:                            # 빨간색일때, 뒤집기
            pieces = pieces[::-1]
    else:                                               # 파란색이거나 좌표 범위를 벗어나는 경우
        y, x, _ = status[num]                           # 그 자리에 유지

    piece[y][x].extend(pieces)
    direction = change_direction(direction)
    status[num] = (y, x, direction)
    change_status(y, x, pieces)

    return y, x


def change_status(y: int, x: int, pieces: list[int]) -> None:
    '''
    이동하는 말의 위에 있는 모든 말들 상태 정보 변경
        params:
            y: 새로 이동하는 행 좌표
            x: 새로 이동하는 열 좌표
            pieces: 이동하는 말들 목록
    '''
    for p in pieces:
        _, __, d = status[p]
        status[p] = (y, x, d)


def change_direction(direction: int) -> int:
    """
    현재 방향의 반대 방향 반환
        params:
            direction: 현재 진행 방향
        returns:
            반대 방향
    """
    if direction == 0:
        return 1
    elif direction == 1:
        return 0
    elif direction == 2:
        return 3
    elif direction == 3:
        return 2


def solution() -> int:
    '''
    시뮬레이션
        returns:
            진행한 턴(turn) 또는 -1
    '''
    turn = 0

    while True:
        turn += 1
        for k in range(K):
            y, x, direction = status[k]             # 현재 말의 좌표값, 진행 방향
            r = y + dr[direction]                   # 새로운 좌표
            c = x + dc[direction]

            pieces = get_pieces(k, y, x)            # 이동할 말 목록을 가져옴
            if 0 <= r < N and 0 <= c < N:           # 정상 범위의 이동일때, 다음 좌표 색상별 함수 실행
                if board[r][c] == 0:
                    move_to_white(pieces, r, c)
                elif board[r][c] == 1:
                    move_to_red(pieces, r, c)
                elif board[r][c] == 2:
                    r -= dr[direction] * 2          # 진행 반대 방향으로 한칸 이동
                    c -= dc[direction] * 2
                    r, c = move_to_blue(pieces, r, c, k, direction)
            else:
                r -= dr[direction] * 2
                c -= dc[direction] * 2
                r, c = move_to_blue(pieces, r, c, k, direction)

            if len(piece[r][c]) >= 4:               # 이동한 좌표가 말 4개 이상이면 종료
                return turn

        if turn > 1000:                             # 턴이 1000회 초과시 -1 반환
            return -1


# 화살표 방향
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

# 입력값
N, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 좌표별 말의 현황
piece = [[[] for _ in range(N)] for _ in range(N)]

# 각 말별 현재 좌표 및 진행 방향 정보
status = {}

# 입력값
for i in range(K):
    y, x, d = map(int, sys.stdin.readline().split())
    piece[y-1][x-1].append(i)
    status[i] = (y-1, x-1, d-1)

print(solution())
