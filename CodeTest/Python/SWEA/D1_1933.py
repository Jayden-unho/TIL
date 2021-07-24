number = int(input())
answer = []

for i in range(1,number+1):
    if number%i == 0:
        answer.append(str(i))

print(' '.join(answer))