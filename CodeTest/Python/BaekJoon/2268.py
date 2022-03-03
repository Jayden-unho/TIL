import sys
from math import log2, ceil
sys.stdin = open('input.txt')

def make_linked(node, left, right):                     # 배열의 숫자가 세그먼트 트리의 어느 인덱스에 저장되었는지 알기 위함
    if left >= right:
        linked[left] = node                             # 리프노드인 경우 배열에 저장
        return

    make_linked(node*2, left, (left+right)//2)          # 왼쪽 노드들 탐색
    make_linked(node*2+1, (left+right)//2+1, right)     # 오른쪽 노드들 탐색
    return

def query(node, left, right, start, end):                                   # 탐색
    if start <= left and right <= end:                                      # 찾으려는 범위에 완전히 속하면 현재 노드의 값 반환
        return segment_tree[node]       
    elif end < left or right < start:                                       # 찾으려는 범위가 속하지 않으면 0 반환
        return 0

    left_nodes = query(node*2, left, (left+right)//2, start, end)           # 왼쪽 노드들 탐색
    right_nodes = query(node*2+1, (left+right)//2+1, right, start, end)     # 오른쪽 노드들 탐색
    return left_nodes + right_nodes                                         # 일부만 겹치면 왼쪽 노드와 오른쪽 노드에서 겹치는거 찾아서 값 반환

def modify(node):
    if node <= 0:                                                           # 루트노드까지 모두 바꿨으면 종료
        return

    segment_tree[node] = segment_tree[node*2] + segment_tree[node*2+1]      # 자식 노드들의 합
    modify(node//2)                                                         # 부모 노드 탐색

N, M = map(int, sys.stdin.readline().split())                   # 숫자의 개수, 명령의 개수
segment_tree = [0] * 2**(ceil(log2(N))+1)                       # 세그먼트 트리 초기화
linked = [0] * (N+1)                                            # 배열의 숫자별로 세그먼트 트리 리프노드의 인덱스

make_linked(1, 1, N)                                            # 위치 찾기

for _ in range(M):
    command, a, b = map(int, sys.stdin.readline().split())

    if not command:                         # 합을 구할때
        if a > b:                           # b가 더 크면 a와 스왑
            a, b = b, a
        print(query(1, 1, N, a, b))         # 탐색
    else:
        segment_tree[linked[a]] = b         # 배열의 숫자 값 변경
        modify(linked[a]//2)                # 부모 노드들의 값 변경