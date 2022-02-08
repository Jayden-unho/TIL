import sys
sys.stdin = open('input.txt')

S = sys.stdin.readline().strip()
P = sys.stdin.readline().strip()
answer = 0

s_idx, p_idx = 0, 0
while s_idx <= len(S)-len(P):
    while p_idx < len(P) and S[s_idx] == P[p_idx]:
        s_idx += 1
        p_idx += 1
        if p_idx >= len(P):
            answer = 1
    
    s_idx += 1
    if p_idx:
        s_idx += p_idx - 1
        p_idx = 0

print(answer)