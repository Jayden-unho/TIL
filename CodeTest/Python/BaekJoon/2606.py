import sys



number = int(sys.stdin.readline())
edge = int(sys.stdin.readline())
linked = [[] for _ in range(number+1)]

# 서로 연결된 명단을 리스트로 작성 양방향으로 저장
for _ in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    linked[a].append(b)
    linked[b].append(a)


# DFS
visited = [0] * (number+1)
dfs_stack = [1]
visited[1] = 1

cnt = 0

while dfs_stack:
    node = dfs_stack.pop()
    for e in linked[node]:
        if not visited[e]:
            dfs_stack.append(e)
            visited[e] = 1
            cnt += 1
            
print(cnt)