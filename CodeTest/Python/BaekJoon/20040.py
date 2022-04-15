import sys
sys.stdin = open('input.txt')

def find(x):                                            # 최상위 부모 노드 탐색
    if x != s[x]:                                       # 현재 노드가 최상위가 아니면
        x = find(s[x])                                  # 최상위 부모 탐색
    return x

def union_set(x, y):                                    # 두개의 노드를 서로 합침
    x = find(x)                                         # x의 최상위 부모를 찾음
    y = find(y)                                         # y의 최상위 부모를 찾음

    if x != y:                                          # 서로 최상위 부모가 다르면
        s[y] = find(x)                                  # 하나로 합침
        return False
    else:                                               # 최상위 부모가 같다면 사이클 형성
        return True

N, M = map(int, sys.stdin.readline().split())           # 노드의 개수, 간선의 개수
s = list(range(N))                                      # 서로소 집합 구분을 위한 리스트

for i in range(1, M+1):
    a, b = map(int, sys.stdin.readline().split())       # 두개의 노드
    
    if a > b:                                           # a와 b 중 a가 큰값이 되도록 설정
        a, b = b, a

    if union_set(a, b):                                 # a와 b를 합침
        print(i)                                        # 사이클 발견되면 종료
        break
else:                                                   # 사이클이 없는 경우
    print(0)