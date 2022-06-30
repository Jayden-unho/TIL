import sys
sys.stdin = open('input.txt')

def solution():                                             # 터질 뿌요의 좌표를 찾는 함수
    visited = [[0] * 6 for _ in range(12)]                  # 좌표 탐색 여부 판별
    pop_list = []                                           # 이번 턴에 터질 뿌요의 좌표 리스트

    for k, v in puyo.items():                               # 뿌요(딕셔너리) 탐색
        if visited[k[0]][k[1]]:                             # 이미 확인한거면 다음 탐색
            continue
        
        coors = []                                          # 현재 뿌요와 연결된 뿌요 리스트
        stack = [k]                                         # 탐색
        while stack:
            y, x = stack.pop()
            if not visited[y][x]:
                coors.append((y, x))                        # 연결된 뿌요 리스트에 추가
                visited[y][x] = 1                           # 좌표 방문 처리
                for k in range(4):
                    r = y + dr[k]
                    c = x + dc[k]

                    if 0 <= r < 12 and 0 <= c < 6 and puyo.get((r, c), False) == v:     # 동일한 색상일 경우에만 추가 탐색
                        stack.append((r, c))
                        
        if len(coors) >= 4:                                 # 현재 뿌요 포함하여 연결된 뿌요가 4개 이상이면
            pop_list.extend(coors)                          # 이번 턴에 터질 뿌요의 리스트에 추가
    
    return pop_list                                         # 터질 뿌요 리스트 반환


def gravity():                                              # 중력 구현
    new_puyo = {}                                           # 중력이 적용된 새로운 딕셔너리

    column = -1                                             # 탐색할 컬럼의 인덱스
    for k in sorted(puyo.keys(), key=lambda x: (x[1], x[0]), reverse=True):     # 열과 행을 내림차순으로 정렬
        v = puyo[k]
        if column != k[1]:                                  # 새로운 열 탐색이면
            column = k[1]                                   # 열 인덱스 새로 지정, 바닥 행의 인덱스 초기화
            bottom_y = 11

        if bottom_y != k[0]:                                # 바닥에 있는 뿌요가 아닌 경우
            new_puyo[(bottom_y, column)] = v                # 바닥으로 이동
        else:                                               # 바닥에 있는 경우
            new_puyo[k] = v                                 # 그냥 추가
        bottom_y -= 1                                       # 행 인덱스 1씩 감소

    return new_puyo                                         # 새로운 뿌요 좌표 반환


dr = [-1, 0, 1, 0]                          # 위 오른쪽 아래 왼쪽
dc = [0, 1, 0, -1]

field = [list(sys.stdin.readline().strip()) for _ in range(12)]     # 입력 정보
puyo = {}                                                           # 뿌요들이 있는 좌표(키) : 색상(값)
answer = 0                                                          # 연쇄 카운트

for i in range(12):                         # 필드를 한번 확인하여
    for j in range(6):                      # 뿌요의 좌표와 색상 정보를 딕셔너리에 저장
        if field[i][j] != '.':
            puyo[(i, j)] = field[i][j]

while True:         
    pop_puyo = solution()       # 한번의 턴에 터지는 뿌요들의 좌표 찾기
    
    if not pop_puyo:            # 터질 뿌요가 없다면 종료
        break
    
    answer += 1                 # 연쇄 증가
    for k in pop_puyo:          # 뿌요들 터트리기
        puyo.pop(k)
    
    puyo = gravity()            # 중력 작용
    
print(answer)