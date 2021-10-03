import sys
sys.stdin = open('input.txt')


""" 
아래 경우는 가능한가 불가능한가
---  ---
   \/

"""

def solution(i, j):
    height = 10
    cnt = 0

    for k in range(N):
        if land[i[k]][j[k]] == height:          # 현재 칸이 이전 칸과 높이가 같을때
            cnt += 1
        elif cnt >= 0:
            if land[i[k]][j[k]] < height:       # 현재 칸이 이전 칸보다 나즐때
                cnt = -X+1
                height = land[i[k]][j[k]]
                if not k:
                    cnt += X
                elif abs(land[i[k]][j[k]] - height) > 1:
                    return False
            elif land[i[k]][j[k]] > height:     # 현재 칸이 이전 칸보다 높을때
                if cnt < X:
                    return False
                elif abs(land[i[k]][j[k]] - height) > 1:
                    return False
                else:
                    height = land[i[k]][j[k]]
                    cnt = 1
        else:                       # 경사로가 튀어 나오거나 안에 못 들어가는 경우
            return False
    if cnt < 0:                     # 경사로가 영역 밖으로 튀어 나오는 경우
        return False

    return True


T = int(input())

for tc in range(1, T+1):
    N, X = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for i in range(N):
        wid = solution([i]*N, range(N))
        hei = solution(range(N), [i]*N)
        
        answer += wid + hei

    print('#{} {}'.format(tc, answer))