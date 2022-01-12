import sys
from math import ceil, log2
sys.stdin = open('input.txt')


def init_tree(node, start, end):                                        # 세그먼트 트리 값 할당
    if start >= end:                                                    # 리프 노드 도달시
        segment_tree[node] = num_list[start]                            # 숫자 리스트의 값 추가
        linked[start-1] = node                                          # 각 숫자가 위치한 리프 노드의 인덱스 저장
        return segment_tree[node]                                   
    
    left_nodes = init_tree(node*2, start, (start+end)//2)               # 왼쪽 노드들의 합
    right_nodes = init_tree(node*2 + 1, (start+end)//2 + 1, end)        # 오른쪽 노드들의 합
    segment_tree[node] = left_nodes + right_nodes                       # 현재 노드 값 저장
    
    return segment_tree[node]

def query(node, start, end, left, right):           # 노드 현재 번호, 노드가 저장한 값의 범위, 찾으려는 범위
    if left <= start and end <= right:              # 찾으려는 구역에 속한 경우 현재 노드 값 반환
        return segment_tree[node]
    elif right < start or end < left:               # 찾으려는 구간에 속하지 않은 경우 0 반환
        return 0

    left_nodes = query(node*2, start, (start+end)//2, left, right)          # 일부만 결치는 경우 자식 노드 탐색
    right_nodes = query(node*2 + 1, (start+end)//2 + 1, end, left, right)
    return left_nodes + right_nodes

def update(node):           # 부모 노드들 값 갱신
    if node < 1:            # 루트 노드까지 모두 값 변경한 경우, 종료
        return

    segment_tree[node] = segment_tree[node*2] + segment_tree[node*2 + 1]        # 왼쪽 자식 노드와 오른쪽 자식 노드 합 저장
    update(node//2)                                                             # 부모 노드 탐색


N, Q = map(int, sys.stdin.readline().split())                   # 숫자의 개수, 질의 및 값 갱신의 횟수
num_list = [0] + list(map(int, sys.stdin.readline().split()))   # 숫자 리스트
segment_tree = [0] * 2**(ceil(log2(N)) + 1)                     # 세그먼트 트리 초기화
linked = [0] * N                                                # 각 숫자들이 저장된 리프 노드의 인덱스

init_tree(1, 1, N)                                              # 세그먼트 트리에 값 설정


for _ in range(Q):
    x, y, a, b = map(int, sys.stdin.readline().split())         # 찾으려는 볌위 (x~y), a번째를 b로 변경


    if y < x:                           # y사 더 작으면 x와 교체
        x, y = y, x

    print(query(1, 1, N, x, y))         # 구간합 찾기
    segment_tree[linked[a-1]] = b       # 리프 노드 값 변경 및 부모 노드들 값 갱신
    update(linked[a-1]//2)