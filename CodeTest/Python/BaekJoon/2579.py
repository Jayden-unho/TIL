import sys

'''
#1. 마지막-1 밟은 경우
마지막-3 + 마지막-1 + 마지막

#2. 마지막-2 밟은 경우
마지막-2 + 마지막

위 두가지 경우 중 더 높은 값을 저장하면 됨
'''



num = int(sys.stdin.readline())
stairs = [int(sys.stdin.readline()) for _ in range(num)]
answer = []

# 세번째 계단까지 값을 입력해줌
answer.append(stairs[0])
if num > 1:
    answer.append(stairs[0] + stairs[1])
    if num > 2:
        answer.append(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))

for n in range(4, num+1):
    tmp1 = answer[n-4] + stairs[n-2] + stairs[n-1]
    tmp2 = answer[n-3] + stairs[n-1]
    answer.append(max(tmp1, tmp2))

print(answer[-1])