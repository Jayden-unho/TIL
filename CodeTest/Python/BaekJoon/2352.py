import sys
sys.stdin = open('input.txt')

def solution(left, right, target):
    if left > right:                                                # 탐색 종료
        return left
    
    mid = (left+right) // 2                                         # 중간 인덱스 값

    if answer[mid] < target:                                        # 이분 탐색
        return solution(mid+1, right, target)
    elif answer[mid] > target:
        return solution(left, mid-1, target)

N = int(sys.stdin.readline())                                       # 포트 개수
ports = list(map(int, sys.stdin.readline().split()))                # 각 포트가 연결될 반대편 포트 번호

answer = [ports[0]]                                                 

for i in range(1, N):
    if answer[-1] < ports[i]:                                       # 다음 포트 연결이 꼬이지 않는다면
        answer.append(ports[i])                                     # 정답 목록에 추가
    else:                                                           # 꼬이게 된다면 이분탐색으로 이전값 변경
        answer[solution(0, len(answer)-1, ports[i])] = ports[i]     
    
print(len(answer))