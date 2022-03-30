import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())                           # 공의 개수
infos = []                                              # 공의 정보들
answers = {}                                            # 정답 변수

for idx in range(N):                                    # 공의 정보들 저장
    C, S = map(int, sys.stdin.readline().split())
    infos.append((C, S))

sorted_size = sorted(infos, key=lambda x: (x[1], x[0])) # 공을 사이즈별로, 색상별로 정렬

pre_size = 0                                # 이전 경우의 공의 사이즈
pre_color = 0                               # 이전 경우의 공의 색상
pre_idx = 0                                 # 이전 경우에서 현재 경우보다 작은 사이즈의 인덱스

acc_sum = [[0] for _ in range(N+1)]         # 0번 인덱스 - 공의 사이즈 누적합, 1번 인덱스 이후 - 공의 색상별 누적합
for i in range(N):
    c, s = sorted_size[i]               
    acc_sum[0].append(acc_sum[0][-1] + s)   # 공의 사이즈 누적합
    acc_sum[c].append(acc_sum[c][-1] + s)   # 공의 색상별 사이즈 누적합

    if pre_size == s:                                                   # 이전과 같은 사이즈 공이면
        if pre_color != c:                                              # 이전과 다른 색상일때, (정답은 딕셔너리 변수이므로 같은 색, 같은 사이즈는 한번만 저장하면 됨)
            answers[(c, s)] = acc_sum[0][pre_idx] - acc_sum[c][-1]      # 나보다 작은 사이즈까지의 누적합 - 나와 같은 색상들 누적합 (두 경우에 나의 사이즈 합도 모두 포함되어 있음)
    else:
        answers[(c, s)] = acc_sum[0][-1] - acc_sum[c][-1]               # 사이즈 누적합 - 나와 같은 색상들 누적합
        pre_idx = i + 1                                                 # 사이즈 누적합 인덱스 변경

    pre_size = s                            # 이전 경우의 사이즈와 색상 변경
    pre_color = c


for c, s in infos:
    print(answers[(c, s)])