import sys
sys.setrecursionlimit(10000)

def solution(nodeinfo):
    answer = [[], []]                   # 전위 순회, 후위 순회

    nodeinfo = list(sorted(enumerate(nodeinfo, start=1), key=lambda x: (x[1][1], x[1][0])))     # 루트 노드를 찾기 위해 정렬

    def order(nodes: list):                 # 트리의 순회
        if not nodes:                       # 노드가 없으면 종료
            return

        left_nodes, right_nodes = [], []    # 왼쪽, 오른쪽 자식 노드들
        node = nodes.pop()                  # 현재 노드의 정보 (부모 노드)

        for n in nodes:                     # 노드들의 정보들을 확인
            if n[1][0] < node[1][0]:        # 부모 노드보다 왼쪽에 있으면, 왼쪽 자식 노드에 추가
                left_nodes.append(n)
            else:                           # 오른쪽에 있으면 오른쪽 자식 노드에 추가
                right_nodes.append(n)

        answer[0].append(node[0])           # 전위 순회
        order(left_nodes)                   # 왼쪽, 오른쪽 자식 노드들 재귀하여 탐색
        order(right_nodes)
        answer[1].append(node[0])           # 후위 순회

    order(nodeinfo)                         # 출력

    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))