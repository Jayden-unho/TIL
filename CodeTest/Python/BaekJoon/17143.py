import sys
sys.stdin = open('input.txt')

def move_shark(sharks):
    moved_sharks = {}                               # 상어들 이동 후 정보

    for k, v in sharks.items():
        r, c = k                                    # 상어 좌표
        s, d, z = v                                 # 상어 정보

        if d < 2:                                   # 상하 이동
            r += dr[d] * s                     # 나머지 값만큼 추가 이동
            while r < 0 or r >= R:                  # 좌표 범위를 벗어나는 경우
                if r < 0:                           # 반대방향으로 이동
                    r *= -1
                elif r >= R:
                    r = 2 * R - r - 2
                d = 1 if d == 0 else 0              # 방향 전환

        elif d >= 2:                                # 좌우 이동
            c += dc[d] * s
            while c < 0 or c >= C:
                if c < 0:
                    c *= -1
                elif c >= C:
                    c = 2 * C - c - 2
                d = 3 if d == 2 else 2
        
        if moved_sharks.get((r, c), False):             # 같은 좌표에 이미 상어가 있는 경우
            if moved_sharks[(r, c)][2] < z:             # 현재 상어 크기가 더 클때만
                moved_sharks[(r, c)] = (s, d, z)        # 현재 상어로 덮어씌우기
        else:                                           # 좌표에 상어가 없다면
            moved_sharks[(r, c)] = (s, d, z)            # 상어 추가
    
    return moved_sharks                                 # 새로운 상어 정보 반환

dr = [-1, 1, 0, 0]                                          # 위, 아래, 오른쪽, 왼쪽
dc = [0, 0, 1, -1]

R, C, M = map(int, sys.stdin.readline().split())            # 행, 열 크기, 상어 수
sharks = {}                                                 # 상어들 위치 및 정보
answer = 0
king = 0                                                    # 낚시왕의 위치

for _ in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())  # 좌표, 속력, 이동 방향, 크기
    s %= (R-1) * 2 if d <=2 else (C-1) * 2                  # (이동할 칸 - 1) * 2 로 나눈다
    sharks[(r-1, c-1)] = (s, d-1, z)                        # 좌표를 키로 하고 값은 상어의 정보

while king < C:                                             # 낚시왕이 열을 한칸씩 이동하며 확인
    # 낚시왕과 같은 열에 있는 상어들을 찾은 후, 행의 번호가 낮은 순서대로 나열
    can_catch = sorted(filter(lambda x: x[1] == king, sharks.keys()), key=lambda x: x[0])

    if can_catch:                   # 잡을 수 있는 상어가 있다면
        coor = can_catch[0]         # 가장 낮은 행의 상어 좌표 선택
        answer += sharks[coor][2]   # 상어 잡기
        sharks.pop(coor)            # 상어 삭제
        
    sharks = move_shark(sharks)     # 상어 이동

    king += 1                       # 낚시왕 이동

print(answer)