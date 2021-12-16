""" 
딕셔너리를 이용한 풀이
"""
import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
J = list(map(int, sys.stdin.readline().split()))

pleasures = {0:0}

for i in range(N):
    s = L[i]
    p = J[i]
    tmp = {}
    for pleasure, stamina in pleasures.items():
        ns = s + stamina
        np = p + pleasure
        if ns < pleasures.get(np, 100):
            tmp[np] = ns

    pleasures.update(tmp)

print(max(pleasures.keys()))


"""
1차원 배열을 이용한 냅색(Knapsack) 알고리즘
"""
# import sys
# sys.stdin = open('input.txt')

# N = int(sys.stdin.readline())
# L = list(map(int, sys.stdin.readline().split()))
# J = list(map(int, sys.stdin.readline().split()))

# pleasure = [0 for _ in range(101)]

# for i in range(1, N+1):
#     s = L[i-1]
#     p = J[i-1]
#     for j in range(100, 0, -1):
#         if j > s:
#             pleasure[j] = max(pleasure[j], pleasure[j-s] + p)

# print(pleasure[-1])


"""
2차원 배열을 이용한 냅색(Knapsack) 알고리즘
"""
# import sys
# sys.stdin = open('input.txt')

# N = int(sys.stdin.readline())
# L = list(map(int, sys.stdin.readline().split()))
# J = list(map(int, sys.stdin.readline().split()))

# pleasure = [[0 for _ in range(101)] for _ in range(N+1)]

# for i in range(1, N+1):
#     s = L[i-1]
#     p = J[i-1]
#     for j in range(1, 101):
#         if j <= s:
#             pleasure[i][j] = pleasure[i-1][j]
#         else:
#             pleasure[i][j] = max(pleasure[i-1][j], p + pleasure[i-1][j-s])
            
# print(pleasure[N][100])