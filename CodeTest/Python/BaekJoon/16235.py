import sys
from collections import deque

dr = [-1, -1, -1, 0, 0, 1, 1, 1]                                        # 왼쪽위, 위, 오른쪽위, 왼쪽, 오른쪽, 왼쪽아래, 아래, 오른쪽아래
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

N, M, K = map(int, sys.stdin.readline().split())                        # 땅 크기, 초기 나무 개수, 남은 년도
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]    # 겨울에 추가되는 양분 정보
land = [[5] * N for _ in range(N)]                                      # 초기 땅의 양분 상태
tree = [[deque() for _ in range(N)] for _ in range(N)]                  # 좌표별 나무들 나이 정보

for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())                    # 좌표, 나이
    tree[x-1][y-1].append(z)                                            # 좌표에 나무의 나이 추가

def solution(prevTree):                                                 
    new_tree = [[deque() for _ in range(N)] for _ in range(N)]          # 다음년도에 있을 나무의 나이 정보들

    for y in range(N):                                                  # 모든 좌표 순환 (모든 땅에 양분이 추가 되어야 하므로)
        for x in range(N):
            if not prevTree[y][x]:                                      # 나무가 없는 땅이면, 양분만 추가하고 종료
                land[y][x] += A[y][x]
                continue

            while prevTree[y][x]:                                       
                z = prevTree[y][x].popleft()                            # 가장 어린 나무부터 성장

                if land[y][x] >= z:                                     # 성장 가능하다면
                    land[y][x] -= z                                     # 땅에서 양분 제거
                    new_tree[y][x].append(z+1)                          # 나이 1살 추가하여 내년 나무 정보에 추가

                    if z % 5 == 4:                                      # 1살 추가 후 나이가 5의 배수일때
                        for k in range(8):                              # 내년 주변 땅에 1살의 나무들 추가
                            r = y + dr[k]
                            c = x + dc[k]
                            if 0 <= r < N and 0 <= c < N:
                                new_tree[r][c].appendleft(1)
                else:                                                   # 성장이 불가능할때
                    land[y][x] += z//2                                  # 땅에 양분 제공하고 반복문 종료
                    break

            for z in prevTree[y][x]:                    # 남아있는 모든 나무들을 모두 죽게 되므로 땅에 양분만 추가
                land[y][x] += z//2
                    
            land[y][x] += A[y][x]                       # 로봇이 돌아다니며 땅에 양분 추가
    return new_tree                                     # 내년 나무 정보 반환

while K > 0:                        # 해당 기간이 지날때까지 반복
    tree = solution(tree)
    K -= 1

cnt = 0                             # 각 좌표별 남아있는 나무들 카운트
for i in range(N):
    for j in range(N):
        cnt += len(tree[i][j])
print(cnt)