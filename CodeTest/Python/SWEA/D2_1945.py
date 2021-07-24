testCase = int(input())

for i in range(1, testCase+1):
    in_num = int(input())
    answer = []

    for n in [2,3,5,7,11]:
        j = 0
        while in_num % (n**j) == 0:
            j += 1

        answer.append(str(j-1))    

    print(f'#{i} ', end='')
    print(str.join(" ", answer))