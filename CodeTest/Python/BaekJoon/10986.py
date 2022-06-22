import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())                           # 숫자의 개수, 나눌 수
nums = list(map(lambda x: int(x) % M, sys.stdin.readline().split()))    # 입력 숫자들을 M으로 나눈 나머지들
acc_nums = [0]                                                          # 누적합 초기 0 추가
cnt = [0] * M                                                           # 각 나머지들 개수 기록할 리스트
answer = 0

for i in range(N):
    num = (acc_nums[-1] + nums[i]) % M          # i+1 까지의 누적 합(M으로 나눈 나머지만 기록) 
    acc_nums.append(num)                        
    cnt[num] += 1                               # 나머지 개수 추가
    if not num:                                 # 나머지가 0인 경우에는 i == j 인 경우에 나누어 떨어짐
        answer += 1

for num in cnt:                                 # 나머지의 개수를 이용해 구간별 경우의 수 구하기
    answer += num * (num-1) // 2

print(answer)