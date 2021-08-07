import sys



num = int(sys.stdin.readline())
answer = [0, 1, 2]

for n in range(3, num+1):
    answer.append((answer[n-2] + answer[n-1])%10007)

print(answer[num])