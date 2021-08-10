'''
시작시간이 제일 빠른순으로 정렬하고, 같은 시작시간 중에서 회의 시간이 제일 짧은걸 선택
위의 회의 시간 중간에 들어갈수있는 더 작은 경우의 수가 있다면 채운다
회의가 끝난후 제일 빨리 시작하는 시간을 선택
두번째로 시작하는 시간에서 제일 짧은 회의 선택
반복
'''

import sys



num = int(sys.stdin.readline())
num_dict = {}
answer = 0
end_time = 2**31                                                        # 초기 회의 끝나는 시간 지정

for _ in range(num):                                                # 딕셔너리 형태에 저장  (int)회의 시작 시간 : (list)[회의 끝나는 시간]
    start, end = map(int, sys.stdin.readline().split())
    num_dict[start] = num_dict.get(start, []) + [end]


for k in sorted(num_dict.keys()):                                   # 키 값을 오름차순으로 정렬하여 빨리 시작하는 값부터 가져옴
    value_list = list(sorted(num_dict.get(k)))                      # 해당 키값의 값들을 오름차순으로 정렬
    
    if value_list[0] <= end_time or k >= end_time:
        if value_list[0] <= end_time:
            answer -= 1
        idx = 0
        while k == value_list[idx]:
            answer += 1
            idx += 1

        answer += 1                                                  # 회의 끝나는 시간을 새로 저장
        end_time = value_list[idx]
    
print(answer)