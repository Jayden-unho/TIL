import sys
from itertools import combinations
sys.stdin = open('input.txt')

def solution():                         # 모든 열이 본인 열로 되돌아 오는지 확인
    for c in range(N):                  # 모든 열을 반복하며 확인
        ans = 0                         # 현재 열의 위치 (상대적, 양수이면 오른쪽, 음수는 왼쪽)
        for r in range(H):              # 행이 하나씩 증가
            ans += ladder[r][c+ans]     # 해당 좌표의 값을 더함
        if ans:                         # 변수의 값이 0이 아니라면 본인 열로 되돌아가지 못한것
            return False
    return True                         

N, M, H = map(int, sys.stdin.readline().split())                    # 열, 주어진 가로선, 행의 개수
ladder = [[0] * N for _ in range(H)]                                # 사다리 정보
# 사다리 설치 가능한 목록 (왼쪽 좌표, 오른쪽 좌표)
can = {((i, j), (i, j+1)) for j in range(N-1) for i in range(H)}
answer = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    ladder[a-1][b-1] = 1                            # 해당 좌표에서 오른쪽으로 가는 사다리
    ladder[a-1][b] = -1                             # 해당 좌표에서 왼쪽으로 가는 사다리
    # 가로선이 연속할 수 없으므로, 왼쪽과 본인, 오른쪽의 좌표를 모두 제거
    can.difference_update((((a-1, b-2), (a-1, b-1)), ((a-1, b-1), (a-1, b)), ((a-1, b), (a-1, b+1))))
    
for k in range(4):                          # 최대 3개를 놓을 수 있으므로
    for element in combinations(can, k):    # 가로선을 놓을 수 있는 좌표들로 조합을 구함
        chk = set()                         # 가로선이 연속으로 이어지지 않았는지 확인을 위한 변수
        for e in element:                   
            chk.update(e)                   # 가로선이 연결된 왼쪽, 오른쪽 좌표 추가
            ladder[e[0][0]][e[0][1]] = 1    # 왼쪽 좌표에서는 오른쪽 방향 숫자 추가
            ladder[e[1][0]][e[1][1]] = -1   # 오른쪽 좌표에서는 왼쪽 방향 숫자 추가

        if k * 2 == len(chk):               # 가로선이 연속으로 이어지지 않았다면 (좌표가 겹치는게 없다면)
            if solution():                  # 모든 열이 본인 열로 돌아오는지 확인
                print(k)                    # 정답 출력 및 프로그램 종료
                exit(0)

        for e in element:                   # 오답이므로 가로선 놓은것 되돌리기
            ladder[e[0][0]][e[0][1]] = 0
            ladder[e[1][0]][e[1][1]] = 0
print(-1)                                   # 조건으로 불가능한 경우 출력