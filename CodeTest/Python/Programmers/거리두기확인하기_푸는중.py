from collections import deque
from pprint import pprint

DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]

def bfs(q, visited, place):
    while q:
        y, x = q.popleft()
        for k in range(4):
            r = y + DR[k]
            c = x + DC[k]

            if 0 <= r < 5 and 0 <= c < 5 and not visited[r][c] and place[r][c] != 'X':
                distance = visited[y][x] + 1
                if place[r][c] == 'P' and distance <= 3:
                    return 0
                elif distance <= 3:
                    visited[r][c] = distance
                    q.append((r, c))
            elif 0 <= r < 5 and 0 <= c < 5 and visited[y][x] + 1 <= 3 and place[r][c] == 'P':
                return 0

    return 1


def solution(places):
    answer = []
    
    for place in places:
        visited = [[0]*5 for _ in range(5)]
        people = []

        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append((i, j))
                    visited[i][j] = 1
        
        q = deque(people)
        answer.append(bfs(q, visited, place))

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))