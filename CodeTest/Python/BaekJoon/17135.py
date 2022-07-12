import sys
sys.stdin = open('input.txt')

def get_case(n, ans, prev):         # 궁수 3명이 가능한 위치 구하기
    if n == 0:
        cases.append(ans)
        return
    
    for i in range(prev+1, M):
        get_case(n-1, ans+[i], i)

def solution(c, enemies):                           # 시뮬레이션
    ans = 0                                         # 현재 경우에 제거된 적의 수

    while enemies:                                  # 적이 남아있으면 반복
        targets = [(100, 100, 100)] * 3             # 각 궁수별 화살을 쏠 적과의 거리, 좌표 정보

        for e in enemies:                                       # 모든 적과 궁수들과 서로 거리 비교
            for i in range(3):
                distance = abs(N - e[0]) + abs(c[i] - e[1])     # 궁수와 적과의 거리
                if distance <= D:                               # 사정거리라면
                    prev_dist = targets[i][0]                   # 이전의 타겟과의 거리
                    # 새로운 타겟이 더 가깝거나, 거리 동일할 때 더 왼쪽에 있는 경우
                    if prev_dist > distance or (prev_dist == distance and targets[i][2] > e[1]):
                        targets[i] = (distance, e[0], e[1])     # 새로운 타겟
                    
        removed = set()                             # 제거되는 적들
        for i in range(3):                          
            if targets[i][0] == 100:                # 타겟이 없다면 (초기의 값이라면)
                continue                            # 다음 궁수 확인
            y, x = targets[i][1], targets[i][2]
            enemies.discard((y, x))                 # 적군 제거
            removed.add((y, x))                     # 제거된 적 명단에 추가
        ans += len(removed)                         # 제거된 적의 수 추가
        
        moved_enemies = set()                       # 적들이 새로 움직일 좌표
        for e in enemies:
            if e[0] + 1 < N:
                moved_enemies.add((e[0]+1, e[1]))   # 한칸씩 아래로 이동
        
        enemies = moved_enemies
        
    return ans                                      # 제거된 적의 수 반환

N, M, D = map(int, sys.stdin.readline().split())                            # 행, 열, 공격 거리 제한
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]    # 전장 정보
cases = []                                                                  # 궁수 3명이 가능한 위치들
enemies = set()                                                             # 적의 위치들
answer = 0

for i in range(N):                  # 적의 위치들을 찾음
    for j in range(M):
        if board[i][j]:
            enemies.add((i, j))

get_case(3, [], -1)                 # 궁수들이 위치할 수 있는 좌표들 경우 구하기

for c in cases:
    answer = max(solution(c, enemies.copy()), answer)       # 시뮬레이션

print(answer)