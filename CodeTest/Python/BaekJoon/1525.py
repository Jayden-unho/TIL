import sys
from collections import deque
sys.stdin = open('input.txt')


# 문자열로 된 보드판의 비어있는 좌표값 반환
def get_coors(board: str):
    idx = board.find('0')
    # 행, 열 반환
    return idx // 3, idx % 3


# 좌표를 이동하고 문자열로 변환하여 반환
def move_coors(board: list, from_y: int, from_x: int, to_y: int, to_x: int) -> str:
    # 좌표들을 문자열의 인덱스로 변경
    from_idx = from_y * 3 + from_x
    to_idx = to_y * 3 + to_x

    # 이동 대상이 되는 인덱스의 값들 서로 변경
    board[from_idx], board[to_idx] = board[to_idx], board[from_idx]
    return ''.join(board)


# BFS 탐색
def solution(board: str) -> None:
    q = deque([(board, 0)])

    while q:
        board, ans = q.popleft()

        # 정답을 찾았다면, 변경 횟수 반환
        if board == '123456780':
            return ans

        # 문자열에서 비어있는 좌표값 구하기
        y, x = get_coors(board)
        for k in range(4):
            r = y + dr[k]
            c = x + dc[k]

            if 0 <= r < 3 and 0 <= c < 3:
                # 비어있는 곳을 좌표 이동시키기
                new_board = move_coors(list(board), y, x, r, c)
                # 이전에 탐색했던 경우가 아니라면, 다음 탐색 위해 추가
                if new_board not in visited:
                    q.append((new_board, ans+1))
                    visited.add(new_board)

    # 정답을 찾을 수 없으므로 -1 반환
    return -1


# 상하좌우 이동 위함
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 입력 값
board = ''.join([''.join(sys.stdin.readline().split()) for _ in range(3)])
# 보드판 탐색 여부
visited = set()

print(solution(board))
