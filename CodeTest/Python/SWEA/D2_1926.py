in_num = int(input())
answer = []

for n in range(1, in_num+1):
    three_count = 0
    i = n

    while i > 0:
        if i%10 == 3 or i%10 == 6 or i%10 == 9:
            three_count += 1
        i //= 10
        
    if three_count == 0:
        answer.append(str(n))
    else:
        answer.append('-'*three_count)

print(' '.join(answer))