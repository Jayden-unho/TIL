"""
Python
    Memory - 55 MB
    Time - 3.096 s
"""
import sys
from math import ceil, log2
sys.stdin = open('input.txt')


def initial_tree(node, start, end):                                 # 세그먼트 트리 만들기, 현재 노드 번호 / 범위 시작 / 범위 끝
    if start >= end:                                                # 리프 노드에 도달했을때
        segment_tree[node] = (lst_num[start], lst_num[start])       # 현재 인덱스에 숫자를 넣음 (최솟값, 최댓값)
        return segment_tree[node]                                   # 현재 노드의 최댓값, 최솟값 정보를 반환
    
    left = initial_tree(node*2, start, (start+end)//2)              # 왼쪽 자식 노드 재귀 호출
    right = initial_tree(node*2 + 1, (start+end)//2 + 1, end)       # 오른쪽 자식 노드 재귀 호출

    min_num = min(left[0], right[0])            # 왼쪽, 오른쪽 자식 노드의 최솟값 비교하여 최솟값 도출
    max_num = max(left[1], right[1])            # 왼쪽, 오른쪽 자식 노드의 최댓값을 비교하여 최댓값 도출
    segment_tree[node] = (min_num, max_num)     # 현재 노드에 최솟값, 최댓값 저장
    
    return segment_tree[node]                   # 현재 노드의 최솟값, 최댓값 반환


def query(node, left, right):                                       # 쿼리에 따라 탐색, 현재 노드 / 왼쪽 범위 / 오른쪽 범위
    if left > end or right < start:                                 # 현재 노드가 가진 정보의 범위가 내가 찾으려는 범위와 겹치지 않을때
        return []                                                   # 비어 있는 리스트 반환
    elif start <= left and right <= end:                            # 현재 노드가 가진 정보의 범위가 내가 찾으려는 범위에 완전히 속할때
        return segment_tree[node]                                   # 현재 노드 범위의 최솟값, 최댓값 반환
    
    left_area = query(node*2, left, (left+right)//2)                # 왼쪽 자식 탐색
    right_area = query(node*2 + 1, (left+right)//2 + 1, right)      # 오른쪽 자식 탐색

    if left_area and right_area:                                    # 왼쪽, 오른쪽 자식 모두 값이 있을때
        min_num = min(left_area[0], right_area[0])                  # 최솟값, 최댓값 구하기
        max_num = max(left_area[1], right_area[1])                  
    elif left_area:                                                 # 왼쪽 자식에만 값이 있으면, 왼쪽의 최솟값, 최댓값 저장
        min_num = left_area[0]
        max_num = left_area[1]
    elif right_area:                                                # 오른쪽 자식에만 값이 있으면, 오른쪽의 최솟값, 최댓값 저장
        min_num = right_area[0]
        max_num = right_area[1]
    
    return (min_num, max_num)                                       # 최솟값, 최댓값 반환


N, M = map(int, sys.stdin.readline().split())                       # 노드의 개수, 쿼리의 개수
lst_num = [0] + [int(sys.stdin.readline()) for _ in range(N)]       # 숫자 리스트 변수
segment_tree = [[] for _ in range(2**ceil(log2(N)) * 2)]            # 비어있는 세그먼트 트리 생성

initial_tree(1, 1, N)                                               # 세그먼트 트리 생성

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())             # 찾으려는 범위
    
    min_num, max_num = query(1, 1, N)                               # 최솟값, 최댓값 구하기
    print(min_num, max_num)                                         # 출력