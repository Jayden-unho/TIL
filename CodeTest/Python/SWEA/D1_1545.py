number = int(input())
answer = []

for i in range(number, -1, -1):
    answer.append(str(i))
print(' '.join(answer))