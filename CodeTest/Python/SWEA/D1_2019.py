number = int(input())
answer = []

for i in range(number+1):
    answer.append(str(2**i))
print(' '.join(answer))