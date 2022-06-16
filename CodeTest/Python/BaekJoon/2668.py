import sys
sys.stdin = open('input.txt')

def solution(start):
    global answer

    stack = [start]                             # 스택
    chk_first = []                              # 첫번째 줄에서 선택한 인덱스
    chk_second = []                             # 두번째 줄에서 나온 숫자

    while stack:
        node = stack.pop()
        if node not in chk_first:               # 첫번째 줄에서 선택하지 않은 인덱스이면
            chk_first.append(node)              # 선택한 인덱스 추가
            next = li[node] - 1                 # 두번째 줄의 값
            chk_second.append(next)             # 두번째 줄의 값 추가
            stack.append(next)                  # 다음 탐색을 위해 스택에 값 추가

    if set(chk_first) == set(chk_second):       # 두개의 줄의 숫자 집합이 같은 경우
        answer.extend(chk_first)                # 정답에 추가

N = int(sys.stdin.readline())                           # 숫자의 개수
li = [int(sys.stdin.readline()) for _ in range(N)]      # 첫째줄과 연결된 두번째 줄의 숫자들
answer = []                             

for i in range(N):              # 정답에 없는 숫자들 탐색
    if i not in answer:
        solution(i)

print(len(answer))              # 출력
for a in sorted(answer):
    print(a+1)