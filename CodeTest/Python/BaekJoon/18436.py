import sys
sys.stdin = open('input.txt')

def make_segment_tree(node, start, end):                    # 세그먼트 트리 생성
    if start >= end:                                        # 리프 노드인 경우
        if nums[start] % 2:                                 # 수열 홀수 짝수에 따른 값 기록
            segment_tree[node] = (0, 1)                     # (짝수 개수, 홀수 개수)
        else:                                                       
            segment_tree[node] = (1, 0)
        leaf_nodes[start] = node                            # 해당 수열이 위치한 리프 노드 번호
        return segment_tree[node]                           # 노드의 값 반환

    left = make_segment_tree(node*2, start, (start+end)//2)     # 왼쪽 자식 노드
    right = make_segment_tree(node*2+1, (start+end)//2+1, end)  # 오른쪽 자식 노드
    segment_tree[node] = (left[0]+right[0], left[1]+right[1])   # 자식 노드의 홀수 짝수 개수 합산
    return segment_tree[node]                                   # 노드 반환

def change_num(node):                                           # 값 변환하는 수열의 부모 노드들
    if not node:                                                # 값 변화 함수
        return
    
    left = segment_tree.get(node*2, (0, 0))                     # 왼쪽 자식 노드
    right = segment_tree.get(node*2+1, (0, 0))                  # 오른쪽 자식 노드
    segment_tree[node] = (left[0]+right[0], left[1]+right[1])   # 자식 노드 값 재계산
    change_num(node//2)                                         # 부모 노드도 값 변경

def query(node, start, end):                                    # 쿼리 탐색
    if arg2 < start or arg1 > end:                              # 영역을 아예 벗어나면 0, 0 반환
        return (0, 0)
    elif arg1 <= start and end <= arg2:                         # 영역이 속해있다면
        return segment_tree[node]                               # 노드의 값 반환
    
    left = query(node*2, start, (start+end)//2)                 # 왼쪽 자식 노드
    right = query(node*2+1, (start+end)//2+1, end)              # 오른쪽 자식 노드
    return (left[0]+right[0], left[1]+right[1])                 # 자식 노드의 값 합산

N = int(sys.stdin.readline())                               # 수열의 크기
nums = [0] + list(map(int, sys.stdin.readline().split()))   # 수열의 숫자들
M = int(sys.stdin.readline())                               # 쿼리 개수

segment_tree = {}           # 세그먼트 트리
leaf_nodes = {}             # 각 수열이 속해있는 노드 번호(리프노드)

make_segment_tree(1, 1, N)  # 세그먼트 트리 생성

for _ in range(M):
    command, arg1, arg2 = map(int, sys.stdin.readline().split())

    if command == 1:                        # 수열 값 변경
        node = leaf_nodes[arg1]             # 수열이 속한 노드의 번호
        if arg2 % 2:                        # 홀수로 변경
            segment_tree[node] = (0, 1)
        else:                               # 짝수로 변경
            segment_tree[node] = (1, 0)
        change_num(node//2)                 # 부모 노드 탐색하며 값 변경
    
    else:                                   # 쿼리 탐색 탐색
        print(query(1, 1, N)[command-2])