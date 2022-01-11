import sys
import math
sys.stdin = open('input.txt')

def init_tree(node, start, end):                            # 세그먼트 트리 초기화 (현재 노드의 번호, 노드의 범위 시작, 노드의 범위 끝)
    if start >= end:                                        # 리프 노드에 도달한 경우
        segment_tree[node] = num_li[start]                  # 리프 노드에 숫자 값 넣기
        linked[start-1] = node                              # 연결관계에 리프노드의 인덱스 추가
        return segment_tree[node]                           # 현재 노드의 값 할당
    
    left = init_tree(node*2, start, (start+end)//2)         # 왼쪽 노드들의 곱
    right = init_tree(node*2+1, (start+end)//2+1, end)      # 오른쪽 노드들의 곱
    segment_tree[node] = (left * right) % 1000000007        # 현재 노드의 값을 할당

    return segment_tree[node]                               # 현재 노드 값 반환 

def query(node, start, end, left, right):                   # 쿼리 (현재 노드의 번호, 노드가 가르키는 범위 시작, 범위 끝, 찾으려는 범위의 시작, 끝)
    if left <= start and end <= right:                      # 현재 노드가 찾으려는 범위에 완전히 속할때
        return segment_tree[node]   
    elif left > end or start > right:                       # 현재 노드가 찾으려는 범위에 완전히 속하지 않을때
        return 1

    left_nodes = query(node*2, start, (start+end)//2, left, right)              # 일부만 겹치면 자식 노드 탐색
    right_nodes = query(node*2 + 1, (start+end)//2 + 1, end, left, right)
    return (left_nodes * right_nodes) % 1000000007                              # 값 반환

def update(node):           # 리프 노드의 값 변경에 따른 부모 노드 값 변경
    if node <= 0:
        return

    segment_tree[node] = (segment_tree[node*2] * segment_tree[node*2+1]) % 1000000007
    update(node//2)

N, M, K = map(int, sys.stdin.readline().split())                    # 수의 개수, 변경 횟수, 구간 곱을 구하는 횟수
num_li = [0] + [int(sys.stdin.readline()) for _ in range(N)]        # 숫자 리스트
segment_tree = [0] * 2**(math.ceil(math.log2(N)) + 1)               # 세그먼트 트리 생성
linked = [-1] * N                                                   # 각 숫자별 저장된 리프 노드의 인덱스

init_tree(1, 1, N)

for _ in range(M+K):                                        # 변경 및 곱 구하는 횟수만큼 반복
    a, b, c = map(int, sys.stdin.readline().split())        # 명령의 타입 인덱스, 변경 숫자 / 구하는 구간

    if a == 1:                              # 값 변경의 경우
        idx = linked[b-1]                   # 바꾸려는 값이 위치한 리프노드의 인덱스를 구함
        segment_tree[idx] = c               # 리프 노드 값 변경
        update(idx//2)                      # 부모 노드들 모두 값 변경
    elif a == 2:                            # 쿼리인 경우
        print(query(1, 1, N, b, c))         # 쿼리 조건의 답 구하여 출력
