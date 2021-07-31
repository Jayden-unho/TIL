import sys

number = int(sys.stdin.readline())
answer = []

for n in range(1, number+1):
    answer.append(n)

#1
while len(answer) > 1:
    tmp = []
    for i in range(1, len(answer), 2):
        tmp.append(answer[i])

    if len(answer)%2:
        tmp.append(tmp.pop(0))
    answer = tmp.copy()

#2
# pop(0) 을 사용하지 않는 방법
'''
while len(answer) > 1:
    tmp = []
    last_append = 0
    sign = len(answer)%2

    for i in range(1, len(answer), 2):
        if sign and i == 1:        
            last_append = answer[i]
        else:
            tmp.append(answer[i])
    if sign:
        tmp.append(last_append)

    answer = tmp.copy()
'''

print(answer[0])