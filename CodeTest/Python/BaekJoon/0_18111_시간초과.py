import sys


#1. 시간초과

import sys


height, width, remainBblock = map(int, sys.stdin.readline().split())
land = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]
 

min_sec = 10**10    # 평탄화 하는데 걸리는 최소한의 시간
line = 256       # 최소한의 시간이 소요되는 땅 높이 (기준선)
dif_high = [line-e for elements in land for e in elements]  # 기준선과 땅의 높이 차이 (양수인 경우 높이를 높여야 함, 음수인 경우 높이를 낮춰야 함)

# 높이가 0이 될때까지 반복
while line >= 0:
    # 여분 블럭이 충분하면 진행, 부족하면 pass
    if remainBblock >= sum(dif_high):
        tmp_sec = sum([v if v>=0 else v*-2 for v in dif_high])    # 양수이면 블록을 채우므로 1초, 음수이면 블록 제거이므로 2초
        
        # 이전보다 시간이 더 소요되면 반복 종료
        if min_sec <= tmp_sec:
            line += 1   # 이전에 더 빨랐던 경우는 층이 하나 더 높으므로 1을 더한다
            break
        min_sec = tmp_sec
    
    # 기준선이 0일때 가장 최적인 경우에 기준선 -1 시키기 전에 반복문 탈출
    if line == 0: break

    # 높이가 하나 낮아지므로 값을 줄임
    dif_high = [v-1 if v>1 else v for v in dif_high]
    line -= 1
    

print(min_sec, line)