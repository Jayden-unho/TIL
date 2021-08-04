import sys


'''
DP (Dynamic Programming)
이전에 계산한 결과를 저장해둠
'''


num = int(sys.stdin.readline())

# 초기에 모든 값을 0으로 설정
num_list = [0 for _ in range(num+1)]

# 1은 1번도 연산 할 필요 없으므로 2부터 시작
for n in range(2, num+1):
    # 초기 최소값을 가장 큰수로 지정
    min = 1000000

    # 2로 나눠지면, 현재 수에 2로 나눈 횟수 1번 + 2로 나눠졌을때 값이 갖고 있는 최소 횟수
    if not n%2:
        tmp = 1 + num_list[n//2]
        if min > tmp:
            min = tmp

    # 3로 나눠지면, 현재 수에 3로 나눈 횟수 1번 + 3로 나눠졌을때 값이 갖고 있는 최소 횟수
    if not n%3:
        tmp = 1 + num_list[n//3]
        if min > tmp:
            min = tmp

    # 현재 수에 1 빼는 횟수 1번 + 1을 뺐을때 값이 갖고 있는 최소 횟수    
    tmp = 1 + num_list[n-1]

    if min > tmp:
        min = tmp

    # 가장 작은 횟수를 저장
    num_list[n] = min

print(num_list[num])