import sys



num = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

num_list.sort()
answer = [num_list[0]]

for n in range(1, num):
    answer.append(answer[n-1] + num_list[n])

print(sum(answer))