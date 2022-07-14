import sys
sys.setrecursionlimit(100000000)
sys.stdin = open('input.txt')

def make_segement_tree(node, left, right):
    if left >= right:                               # 리프 노드 도달시
        segment_tree[node] = (nums[left] , left)    # 리프 노드에 각 숫자(높이), 인덱스 기록
        return segment_tree[node]
    
    left_tree = make_segement_tree(node*2, left, (left+right)//2)           # 왼쪽 자식 노드들의 최소 높이
    right_tree = make_segement_tree(node*2+1, (left+right)//2 + 1, right)   # 오른쪽 자식 노드들의 최소 높이
    
    if left_tree[0] < right_tree[0]:            # 왼쪽 자식들이 더 낮은 높이라면
        segment_tree[node] = left_tree          # 왼쪽 자식 노드 기록
    else:                                       
        segment_tree[node] = right_tree         # 오른쪽 자식 노드 기록

    return segment_tree[node]

def query(node, left, right, start, end):       # 구역의 최소 높이와 인덱스 구하기
    if end < left or right < start:             # 속해있지 않다면 최댓값 반환
        return (1e10, -1)
    elif start <= left and right <= end:        # 완전히 속해있다면, 해당 노드의 값 반환
        return segment_tree[node]
    
    left_tree = query(node*2, left, (left+right)//2, start, end)
    right_tree = query(node*2+1, (left+right)//2 + 1, right, start, end)

    if left_tree[0] < right_tree[0]:            # 왼쪽 자식 노드와 오른쪽 자식 노드 비교하여
        return left_tree                        # 더 낮은 높이를 가진 자식 노드 반환
    return right_tree

def solution(left, right):                      
    if left >= right:                           # 너비가 1일 때
        return nums[left]

    h, idx = query(1, 0, N-1, left, right)      # 최소 높이, 그 높이가 해당하는 인덱스
    s1, s2, s3 = h * (right-left+1), 0, 0       # 현재 구역의 가능한 넓이

    if idx-1 >= left:                           # 최소 높이의 왼쪽 부분   
        s2 = solution(left, idx-1)
    if idx+1 <= right:                          # 최소 높이의 오른쪽 부분
        s3 = solution(idx+1, right)

    return max(s1, s2, s3)
    
while True:
    N, *nums = list(map(int, sys.stdin.readline().split()))     # 숫자의 개수, 숫자들

    if not N:                       # 종료
        break

    segment_tree = {}               # 세그먼트 트리 (구역의 최소 높이를 기록)
    make_segement_tree(1, 0, N-1)   # 세그먼트 트리 생성
    
    print(solution(0, N-1))         # 정답 구하기 및 출력