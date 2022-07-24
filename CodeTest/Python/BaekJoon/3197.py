import sys
sys.stdin = open('input.txt')

# 1500 * 1500
def search_ice(y, x):
    stack = [(y, x)]

    while stack:
        y, x = stack.pop()
        if (y, x) not in ice:
            ice.add((y, x))
            for k in range(4):
                r = y + dr[k]
                c = x + dc[k]

                if 0 <= r < R and 0 <= c < C:
                    if lake[r][c] == 'X':
                        stack.append((r, c))
                    elif lake[r][c] == '.':
                        soon_melt.add((y, x))

def melt():
    new_soon_melt = set()
    new_start = set()

    for y, x in soon_melt:
        ice.remove((y, x))

        for k in range(4):
            r = y + dr[k]
            c = x + dc[k]

            if (r, c) in ice and (r, c) not in soon_melt:
                new_soon_melt.add((r, c))
            elif (r, c) in visited:
                new_start.add((y, x))
                
    return new_soon_melt, new_start


def DFS(start):
    stack = list(start)
    
    while stack:
        y, x = stack.pop()
        if (y, x) not in visited:
            visited.add((y, x))
            for k in range(4):
                r = y + dr[k]
                c = x + dc[k]

                if 0 <= r < R and 0 <= c < C and (r, c) not in ice:
                    stack.append((r, c))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

R, C = map(int, sys.stdin.readline().split())                   # 행, 열
lake = [list(sys.stdin.readline().strip()) for _ in range(R)]   # 호수 정보
visited = set()         # 좌표 방문 여부
points = []             # 
ice = set()
soon_melt = set()
answer = 0

for i in range(R):
    for j in range(C):
        if lake[i][j] == 'X' and (i, j) not in ice:
            search_ice(i, j)
        elif lake[i][j] == 'L':
            points.append((i, j))

start = [points.pop()]
end = points.pop()
while True:
    DFS(start)

    soon_melt, start = melt()
    if (end[0], end[1]) in visited:
        print(answer)
        break

    answer += 1