import sys
import heapq
sys.stdin = open('input.txt')

gorilla = {}
answer = 0

for _ in range(int(sys.stdin.readline())):
    command, name, k, *values = list(sys.stdin.readline().split())

    if command == '1':
        values = list(map(lambda x: int(x) * -1, values))
        gorilla[name] = gorilla.get(name, []) + values
    elif command == '2':
        if not gorilla.get(name, False):
            continue

        k = int(k)
        heapq.heapify(gorilla[name])
        while gorilla[name] and k:
            answer -= heapq.heappop(gorilla[name])
            k -= 1

print(answer)
