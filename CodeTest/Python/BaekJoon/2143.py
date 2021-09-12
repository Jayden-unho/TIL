import sys
sys.stdin = open('input.txt')



T = int(sys.stdin.readline())

N = int(sys.stdin.readline())
n_list = [0] + list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
m_list = [0] + list(map(int, sys.stdin.readline().split()))

n_cumsum_dict = {}
m_cumsum_dict = {}
answer = 0

for idx in range(1, N+1):
    n_list[idx] = n_list[idx] + n_list[idx-1]
    for j in range(1, idx+1):
        tmp = n_list[idx] - n_list[j-1]
        n_cumsum_dict[tmp] = n_cumsum_dict.get(tmp, 0) + 1

for idx in range(1, M+1):
    m_list[idx] = m_list[idx] + m_list[idx-1]
    for j in range(1, idx+1):
        tmp = m_list[idx] - m_list[j-1]
        m_cumsum_dict[tmp] = m_cumsum_dict.get(tmp, 0) + 1

for k in n_cumsum_dict:
    answer += m_cumsum_dict.get(T - k, 0) * n_cumsum_dict[k]

print(answer)