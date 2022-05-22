import sys
sys.stdin = open('input.txt')

def solution(c):
    prev = c.pop()                              # 이전 땅의 높이
    stack = [prev]                              # 경사로를 놓을 수 있는 여분의 땅

    while c:                                    # 다음 땅이 남아있다면
        next = c.pop()                          # 다음 땅의 높이

        if prev == next:                        # 이전 땅과 높이가 같으면 스택에 경사로
            stack.append(next)                  # 여분땅 추가
        elif prev == next - 1:                  # 현재가 이전보다 한칸 높으면
            for k in range(L):                  # 이전 땅들이 동일한 높이로 L 만큼 필요
                if len(stack) < L:              # L 보다 적다면 불가능한 길
                    return False
            stack.clear()                       # 경사로를 놓았으므로 이전땅 사용불가로 스택 정리
            stack.append(next)                  # 다음을 위해 현재 땅 스택에 추가
        elif prev == next + 1:                  # 이전 땅보다 경사로가 낮다면
            for k in range(L-1):                                
                if not c or c.pop() != next:    # 앞으로 땅이 경사로 길이 보다 적고, 다음 땅들이 모두 높이가 같지 않다면
                    return False                # 불가능한 길
            stack.clear()                       # 스택 정리
        else:                                   # 높이 차이가 1보다 크면 불가능한 길
            return False
        prev = next

    return True


N, L = map(int, sys.stdin.readline().split())                               # 배열의 길이, 경사로 길이
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]    # 보드판
cases = []                          # 지나갈 길의 경우들
answer = 0                          # 가능한 길

for i in range(N):
    tmp = []
    for j in range(N):
        tmp.append(board[j][i])     # 열
    cases.append(board[i][:])       # 행
    cases.append(tmp[:])

for element in cases:
    if solution(element):           # 경사로를 이용하여 지나갈 수 있는지 확인
        answer += 1

print(answer)