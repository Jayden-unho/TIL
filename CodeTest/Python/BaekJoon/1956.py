import sys
sys.stdin = open('input.txt')

V, E = map(int, sys.stdin.readline().split())                                       # 마을, 도로 개수
distance = [[1e10] * V for _ in range(V)]                                           # 마을에서 다른 마을로 가는 최소 거리
answer = 1e10                                                                       # 최소 길이 사이클의 값

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    distance[a-1][b-1] = c                                                          # a 마을 ->  b 마을 거리

for k in range(V):
    for i in range(V):
        for j in range(V):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])   # i -> j 이동시, 서로 연결된 도로가 더 짧은지
                                                                                    # 다른 마을을 거쳐서 이동하는게 더 짧은지 비교 후 더 짧은 도로 선택

for i in range(V):                          
    answer = min(answer, distance[i][i])            # 출발지에서 다시 돌아오는 경우의 최소 도로 길이를 저장

print(answer if answer != 1e10 else -1)             # 사이클이 존재하지 않으면 -1 출력