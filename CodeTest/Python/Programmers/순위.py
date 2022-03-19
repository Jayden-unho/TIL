def solution(n, results):
    answer = 0
    players = [[[], []] for _ in range(n)]       # 내가 이긴 선수, 나를 이긴 선수

    def search(start, result):
        stack = [start]
        visited = [0] * n
        cnt = -1

        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] += 1
                cnt += 1
                for p in players[node][1 if result == 'winner' else 0]:
                    stack.append(p)
        
        return cnt

    for result in results:
        win, loss = result
        players[win-1][0].append(loss-1)
        players[loss-1][1].append(win-1)

    for idx in range(n):
        if n-1 == search(idx, 'winner') + search(idx, 'loser'):
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))