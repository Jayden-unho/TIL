'''
1. 큰 숫자 *2 크기의 리스트를 초기화 - 모든 값 0으로 큰 숫자 * 2가 이동 가능한 최대 경우의 수이므로
2. 위의 리스트의 값은, 해당 숫자로 몇번만에 갈수있는지 최소 횟수를 넣는다.
3. 최소 이동 가능한 3가지 경우에서 모두 다음 단계 숫자로 이동시킴, 반복
=> 
Graph Search - BFS
각 숫자에서 -1, +1, *2 했을때 이동하는 숫자를 리스트 형태로 저장하여
너비 우선 탐색 -> 깊이를 한단계 들어갈때마다 카운트 + 1 -> 목적 숫자에 도달하면 종료
'''

import sys
from collections import deque



def bfs_func(start, k, high):
    stack = deque([start])                      # 큐 사용
    last = start                                # 해당 깊이의 마지막 노드를 저장하는 변수
    result = 1                                  # 걸리는 시간 초

    while stack:
        node = stack.popleft()                  
        if node < high*2 and not visited[node]: # 인덱스 에러 방지와 방문하지 않았다면
            visited[node] = True
            tmp = move_list[node]               # 새로 이동할 위치들이 담긴 리스트
            stack.extend(tmp)                   # 큐에 새로 이동할 위치 추가

            if k in tmp:                        # 새로 이동할 위치에 k 의 값이 있다면 종료
                return result
가
        if node == last:                        # 해당 노드가 해당 깊이의 마지막 노드일때
            result += 1                         # 1초 추가
            last = tmp[-1]                      # 다음 깊이의 마지막 노드 추가
    
    return '이동 불가'
        


n, k = map(int, sys.stdin.readline().split())
high = max(n, k)

move_list = [[x-1, x+1, x*2] for x in range(high * 2)]  # 현재위치에서 1초뒤 움직일 수 있는 위치
visited = [False] * (high * 2)                          # 위치 방문 여부

if n == k:                                              # 같은 위치에 있다면 0초만에 만남
    answer = 0
else:                                                   # 서로 다른 위치이면 bfs 탐색
    answer = bfs_func(n, k, high)

print(answer)