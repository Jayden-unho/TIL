import sys  
from bisect import bisect_left
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())                           # 용액의 수
num_li = list(map(int, sys.stdin.readline().split()))   # 용액들의 정보 (오름차순)
diff = 1e15                                             # 용액을 혼합했을 경우의 합산값
answer = []                                             # 정답 리스트

for i in range(N):                                      # 용액들을 순서대로 확인
    idx = bisect_left(num_li, -num_li[i])               # 특성 값을 0을 만들기 위해 -1을 곱한 값이 리스트에 들어갈 수 있는 위치를 찾는다

    for j in range(-1, 2):                              # 찾은 인덱스 앞과 뒤의 인덱스들을 모두 현재 용액과 합쳐본다
        if 0 <= j+idx < N and i != j+idx:               # 인덱스가 리스트 범위 내의 값이여야하고, 동일한 용액이면 안됨
            op_num = num_li[j+idx]              
            if abs(num_li[i] + op_num) <= diff:         # 두개의 용액을 합친 특성값의 절댓값이 가장 작은 값이면
                diff = abs(num_li[i] + op_num)          # 특성값 및 정답 리스트 갱신
                answer = [num_li[i], op_num]

print(*sorted(answer))