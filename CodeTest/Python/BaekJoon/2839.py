import sys

num = int(sys.stdin.readline().rstrip())
answer = 5000
tmp = 0

for i in range(num//5+1):
    for j in range(num//3+1):
        tmp = i*5 + j*3
        
        if tmp==num and answer>i+j:
            answer = i+j

if answer == 5000: print(-1)
else: print(answer)