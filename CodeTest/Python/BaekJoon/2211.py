import sys
import heapq
sys.stdin = open('input.txt')

def solution(start):
    h = [(0, start, start)]                                 # 거리, 도착 컴퓨터 번호, 출발 컴퓨터 번호

    while h:
        node = heapq.heappop(h)
        if distance[node[1]] == -1:                         # 컴퓨터 거리 탐색 안되었다면
            distance[node[1]] = node[0]                     # 최소 거리 기록
            answer.append((node[2]+1, node[1]+1))           # 출발 컴퓨터 번호, 도착 컴퓨터 번호 기록
            for next in linked[node[1]]:                    # 현재 컴퓨터와 연결된 다음 컴퓨터들 거리 추가하여 탐색
                heapq.heappush(h, (node[0] + next[0], next[1], node[1]))

N, M = map(int, sys.stdin.readline().split())               # 컴퓨터 개수, 회선(연결) 개수
linked = [[] for _ in range(N)]                             # 컴퓨터간 연결 정보
distance = [-1] * N                                         # 각 컴퓨터간 통신 최소 시간
answer = []                                                 # 복구할 회선 정보

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    linked[A-1].append((C, B-1))                            # 양방향 통신이므로 두 컴퓨터에 연결 관계 기록
    linked[B-1].append((C, A-1))

solution(0)                                                 # 1번 컴퓨터 보안 시스템 설치

print(len(answer)-1)
for i in range(1, len(answer)):
    print(*answer[i])