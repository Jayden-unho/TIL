import sys



num = int(sys.stdin.readline())
num_list = []
fact = 1
answer = -1

# factorial claculate
for n in range(1, num+1):
    fact *= n

# 각 자리숫자를 리스트에 저장
while fact:
    num_list.append(fact%10)
    fact //= 10

# 거꾸로
num_list.reverse()

tmp = 0
while not tmp:
    tmp = num_list.pop()
    answer += 1

print(answer)