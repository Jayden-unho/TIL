import sys
from collections import deque
sys.stdin = open('input.txt')

def solution():
    q = deque([(0, 0)])                 # 처음 A, B 물통은 비어있음

    while q:
        a, b = q.popleft()              # 현재 A, B 바구니 물의 양
        c = C - a - b                   # C 바구니 물의 양

        if not a:                       # A 바구니가 비어있다면, 정답에 추가
            answer.add(c)
        
        for element in [(a + min(c, A-a), b), (a, b + min(c, B-b)),         # C -> A, C -> B 바구니로 물을 옮김
            (a + min(b, A-a), b - min(b, A-a)), (a, b - min(b, C-c)),       # B -> A, B -> C 바구니로 물을 옮김
            (a - min(a, B-b), b + min(a, B-b)), (a - min(a, C-c), b)]:      # A -> B, A -> C 바구니로 물을 옮김
            
            if not visited.get((element[0], element[1]), False):            # A 바구니와 B 바구니에 남은 물의 양을 탐색하지 않았으면
                visited[(element[0], element[1])] = True                    # 탐색 처리
                q.append((element[0], element[1]))                          # 큐에 추가
        
A, B, C = map(int, sys.stdin.readline().split())        # 물통의 최대양
answer = set()                                          # 정답의 집합
visited = {}                                            # A, B 물통에 현재 담겨있는 물의 양을 탐색했는지 여부

solution()

print(*sorted(answer))              # 오름차순 출력