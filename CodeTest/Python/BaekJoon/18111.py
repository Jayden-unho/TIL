import sys



'''
땅을 고르는데 최소한의 소요시간과 높이를 구하기 위해서는 첫번째 경우부터 차례대로 확인을 해봐야한다.
땅을 파는데 2초 / 땅을 쌓는데 1초가 소요된다. 땅을 파는것보다 쌓는 경우에 시간이 조금 더 적으므로 땅을 가장 많이 쌓는 경우부터 시작점을 잡는다
시작 높이를 땅중에 가장 높은 곳을 선택하고 다음 순환때 높이를 -1씩 진행한다.

1. 땅의 높이를 정했을때 1차적으로 그 높이를 만들기 위해 땅을 파서 여분 블록에 추가한다.
1-1. 땅을 쌓아야 하는 경우의 수가 남은 블록보다 적은지 확인한다. (블록이 부족하면 다음 순환 진행)
2. 땅을 쌓을 수 있으면 소요되는 시간과 땅의 높이 임시변수에 저장
3. 임시변수와 지난 순환때 결과값 서로 비교
4. 지난 순환보다 시간이 더 소요되는 순간 반복문 종료 
'''

height, width, remain_block = map(int, sys.stdin.readline().split())
in_height_list = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]

min_sec = 10**15
answer = 0

land = {}
block = 0
for i in in_height_list:
    for j in i:
        land[j] = land.get(j, 0) + 1
        block += j
remain_block -= j

for line in range(257):
    if remain_block >= 0:
        sec = 0

        for k, v in land.items():
            if line >= k:
                sec += (line-k) * v
            else:
                sec += (k-line) * v * 2
        
        if min_sec > sec:
            min_sec = sec
            answer = line

    remain_block += height * width

print(min_sec, answer)

#1. 시간초과
'''
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
'''