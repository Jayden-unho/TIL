"""
Memory - 29200 kb
Time - 6472 ms

브루트포스 , 순열 ,
시간초과 ->  1. 1001, 0110 <- 같은 경우로 중복 제거 필요 -> 
            2. 가지치기? -> 파라미터로 정답값 넣어야 함 - 뒤로 가서 값이 달라질수있어서 섣부른 가지치기 x
"""

import sys
sys.stdin = open('input.txt')


def solution(idx, remain):
    global answer

    if remain <= 0:             # 하나의 팀이 만들어지면     return [1,1,0,0] , [1,0,1,0]
        left, right = 0, 0      # 1 team, 2 team
    
        for i in range(N):
            for j in range(i+1, N):
                if visited[i] and visited[j]:      # 1 team
                    left += board[i][j] + board[j][i]
                elif not visited[i] and not visited[j]:               # 2 team
                    right += board[i][j] + board[j][i]
        
        if answer > abs(left-right):
            answer = abs(left-right)

        return

    elif idx >= N:          # 범위 벗어나면
        return


    visited[idx] = 1
    solution(idx+1, remain-1)
    visited[idx] = 0
    solution(idx+1, remain)


N = int(sys.stdin.readline())                                                   # 사람 수
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]        # 점수판
visited = [0] * N                                                               # 한팀에 속한 여부
answer = 1e10

solution(0, N//2)

print(answer)