import sys



n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    a = int(sys.stdin.readline())
    
    if a == 0:
        pass
    else:
        heap.append(a)