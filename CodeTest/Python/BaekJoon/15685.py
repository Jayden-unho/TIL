import sys
sys.stdin = open('input.txt')

def dragon_curve(n, dragon):                            # 남은 세대, 이전의 드래곤 커브
    if not n:                                           # 세대가 모두 진행되었다면 드래곤 커브 반환
        return dragon

    standard = dragon[-1]                               # 끝점은 항상 리스트의 마지막 요소
    new_dragon = []                                     # 90도 회전한 다음 세대의 좌표들
    for idx in range(len(dragon)-2, -1, -1):            # 끝점을 제외한 드래곤 커브 반복
        x, y = dragon[idx]

        diff_x = standard[0] - x                        # 끝점과 비교하여 각 좌표간의 거리 구하기
        diff_y = standard[1] - y

                                                        # 90도 회전한 새로운 좌표는
        nx = standard[0] + diff_y                       # x 좌표는 y좌표의 증가/감소량 만큼 증가/감소
        ny = standard[1] + (diff_x * -1)                # y 좌표는 x좌표의 증가/감소량 만큼 감소/증가

        new_dragon.append((nx, ny))                     # 새로운 좌표 추가
    
    return dragon_curve(n-1, dragon + new_dragon)       # 재귀 호출

dx = [1, 0, -1, 0]                                          # 오른쪽, 위, 왼쪽, 아래
dy = [0, -1, 0, 1]                                          

N = int(sys.stdin.readline())                               # 커브의 개수
dragons = set()                                             # 드래곤 커브의 좌표들
answer = 0

for _ in range(N):
    x, y, d, g = map(int, sys.stdin.readline().split())     # 좌표, 시작 방향, 세대

    nx = x + dx[d]                                          # 시작 방향에 따른 끝점
    ny = y + dy[d]

    dragons.update(dragon_curve(g, [(x, y), (nx, ny)]))     # 세대만큼 드래곤 커브 진행 후
                                                            # 드래곤 커브 좌표에 추가

for x, y in dragons:                        # 드래곤 커브의 좌표들을 모두 반복하며 정답 개수 찾기
    for k in [(1, 0), (0, 1), (1, 1)]:      # 1x1 사각형의 꼭지점 탐색
        cx = x + k[0]
        cy = y + k[1]

        if (cx, cy) not in dragons:         # 없다면 다음 좌표 탐색을 위해 종료
            break
    else:                                   # 모두 있다면, 정답 추가
        answer += 1

print(answer)