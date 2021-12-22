import sys
from math import log2, ceil
sys.stdin = open('input.txt')


def initial_tree(node, left, right):                                    # 현재 노드 / 범위 시작 / 범위 끝
    if left >= right:                                                   # 리프 노드일때
        segment_tree[node] = lst_num[left]                              # 현재 노드에 숫자 값 할당
        return segment_tree[node]                                       # 할당된 현재 노드의 값 반환
    
    left_node = initial_tree(node*2, left, (left+right)//2)             # 왼쪽 자식 노드 재귀 호출
    right_node = initial_tree(node*2 + 1, (left+right)//2 + 1, right)   # 오른쪽 자식 노드 재귀 호출
    segment_tree[node] = min(left_node, right_node)                     # 왼쪽, 오른쪽 자식 노드의 값 중 최솟값을 현재 노드에 할당
    
    return segment_tree[node]                                           # 할당 된 현재 노드의 값 반환


def query(node, left, right):                                           # 현재 노드 / 범위 시작 / 범위 끝
    if left > end or right < start:                                     # 질의가 요청하는 범위와 하나도 일치하지 않을때
        return 1e10                                                     # 노드 값으로 올수 없는 최댓값 반환
    elif start <= left and right <= end:                                # 현재 노드의 범위가 질의가 요청하는 범위 안에 완전히 속할때
        return segment_tree[node]                                       # 현재 노드의 값 반환
    
    left_node = query(node*2, left, (left+right)//2)                    # 왼쪽, 오른쪽 자식 노드 탐색
    right_node = query(node*2 + 1, (left+right)//2 + 1, right)
    
    return min(left_node, right_node)                                   # 왼쪽, 오른쪽 자식 노드의 값 중 최솟값 반환


N, M = map(int, sys.stdin.readline().split())                   # 노드의 개수, 질의 개수
lst_num = [0] + [int(sys.stdin.readline()) for _ in range(N)]   # 숫자들 리스트 변수
segment_tree = [0] * 2**ceil(log2(N)) * 2                       # 세그먼트 트리 초기화

initial_tree(1, 1, N)                                           # 세그먼트 트리 내부 값 할당

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())         # 질의 범위

    print(query(1, 1, N))                                       # 출력