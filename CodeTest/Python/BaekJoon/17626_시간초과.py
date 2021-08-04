import sys
import math

number = int(sys.stdin.readline())

answer = [0] * (number+1)
answer[0], answer[1] = 0, 1

for i in range(2, number+1):
    if i == int(math.sqrt(i))**2:
        answer[i] = 1
    else:
        answer[i] = i

for i in range(2, number+1):
    for j in range(1, int(math.sqrt(i))+1):
        answer[i] = min(answer[i], answer[j*j] + answer[i-j*j])

print(answer[number])