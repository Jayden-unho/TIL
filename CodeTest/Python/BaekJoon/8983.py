import sys
sys.stdin = open('input.txt')

def solution(left, right, targets):                     # 반복문 이용한 이분 탐색
    while left <= right:
        mid = (left+right) // 2                         # 탐색할 사대의 인덱스

        if targets[0] <= sites[mid] <= targets[1]:      # 현재 사대가 사정거리 범위 안에 포함된다면
            return True                                 # true 반환
        elif sites[mid] <= targets[0]:                  # 사정거리 범위 밖이라면
            left = mid + 1                              # 다음 탐색을 위한 인덱스 조정
        elif sites[mid] >= targets[1]:
            right = mid - 1
    return False                                        # 모든 사대가 사냥 불가능하면 False 반환

def solution2(left, right, targets):                    # 재귀를 이용한 이분 탐색
    global answer

    if left > right:                                    # 왼쪽 인덱스가 오른쪽 인덱스 보다 크면 종료
        return

    mid = (left+right) // 2                             # 탐색할 인덱스

    if targets[0] <= sites[mid] <= targets[1]:
        answer += 1        
        return
    elif sites[mid] <= targets[0]:                      # 인덱스 조정 후 재귀 호출
        solution2(mid+1, right, targets)
    elif sites[mid] >= targets[1]:
        solution2(left, mid-1, targets)

M, N, L = map(int, sys.stdin.readline().split())                                # 사대 수, 동물 수, 사정거리
sites = sorted(list(map(int, sys.stdin.readline().split())))                    # 사대 위치들 (오름차순 정렬)
animals = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]     # 동물들 위치 좌표
answer = 0

for x, y in animals:                    # 동물 위치 좌표 하나씩 탐색
    x1 = x - (L- y)                     # 사정거리의 최대 거리의 사대 위치
    x2 = x + (L -y)

    if solution(0, M-1, (x1, x2)):      # 사정거리 내에 있는 사대 탐색
        answer += 1                     # 있으면 잡을 수 있는 동물 추가
    
    # solution2(0, M-1, (x1, x2))       # 재귀 이용한 이분 탐색

print(answer)