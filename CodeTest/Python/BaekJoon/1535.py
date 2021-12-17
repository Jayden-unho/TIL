""" 
딕셔너리를 이용한 풀이
"""
import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))        # 사용 하는 체력
J = list(map(int, sys.stdin.readline().split()))        # 얻게 되는 기쁨

pleasures = {0:0}                                       # 초기 얻은 기쁨, 사용하는 체력

for i in range(N):
    s = L[i]                                            # 해당 사람 만나는데 필요한 체력
    p = J[i]                                            # 해당 사람 만나서 얻는 기쁨
    tmp = {}                                            # 추가할 딕셔너리

    for pleasure, stamina in pleasures.items():         # 이전 경우들 모두 순환
        ns = s + stamina                                # 새로운 소모 체력
        np = p + pleasure                               # 새로운 얻는 기쁨
        if ns < pleasures.get(np, 100):                 # 체력 소모가 100이 넘지 않으면 추가
            tmp[np] = ns

    pleasures.update(tmp)

print(max(pleasures.keys())가


"""
1차원 배열을 이용한 냅색(Knapsack) 알고리즘
"""
# import sys
# sys.stdin = open('input.txt')

# N = int(sys.stdin.readline())
# L = list(map(int, sys.stdin.readline().split()))                # 사용 하는 체력
# J = list(map(int, sys.stdin.readline().split()))                # 얻게 되는 기쁨

# pleasure = [0 for _ in range(101)]                              # 열 - 체력

# for i in range(1, N+1):                                         # 한명의 사람 순환
#     s = L[i-1]                                                  # 해당 사람 만나는데 필요한 체력
#     p = J[i-1]                                                  # 해당 사람 만나서 얻는 기쁨

#     for j in range(100, 0, -1):                                 # 체력이 1~100 으로 순환 (2차원 배열과 다르게 역순환)
#                                                                 # j 가 s 보다 커지는 경우 앞에 변경된 값을 따르므로 역순환 해야함
#         if j > s:                                               # 현재 체력으로 사람을 만날 수 있을떄
#             pleasure[j] = max(pleasure[j], pleasure[j-s] + p)   # 사람을 만나는 경우 vs 사람을 안만나는 경우 중 최대 기쁨을 얻는 경우 선택

# print(pleasure[-1])


"""
2차원 배열을 이용한 냅색(Knapsack) 알고리즘
"""
# import sys
# sys.stdin = open('input.txt')

# N = int(sys.stdin.readline())
# L = list(map(int, sys.stdin.readline().split()))                # 사용 되는 체력
# J = list(map(int, sys.stdin.readline().split()))                # 얻게 되는 기쁨

# pleasure = [[0 for _ in range(101)] for _ in range(N+1)]        # 행 - 한명의 사람
#                                                                 # 열 - 체력

# for i in range(1, N+1):                             # 한명의 사람을 순환
#     s = L[i-1]                                      # 해당 사람 만나는데 필요한 체력
#     p = J[i-1]                                      # 해당 사람 만나서 얻는 기쁨
   
#     for j in range(1, 101):                         # 체력이 1~100 일 경우
#         if j <= s:                                  # 현재 남아 있는 체력으로 현재 사람을 만날 수 없는 경우
#             pleasure[i][j] = pleasure[i-1][j]       # 현재 사람을 만나지 않음
#         else:
#             pleasure[i][j] = max(pleasure[i-1][j], p + pleasure[i-1][j-s])      # 남은 체력으로 현재 사람을 만날 수 있으면
#                                                                                 # 사람을 안만나는 경우 vs 만나는 경우 중 더 큰 기쁨을 얻게 되는 결과 선택
            
# print(pleasure[N][100])