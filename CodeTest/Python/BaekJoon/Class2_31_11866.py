import sys

num, term = map(int, sys.stdin.readline().split())
num_list = [i for i in range(1, num+1)]
answer = []
idx = 0

# 리스트에 순차적으로 값에 접근
while num_list:
    idx += term-1 # 주어진 term-1 만큼 인덱스 증가 한번 반복시 값이 하나 제거되어 다른 값들이 인덱스를 한칸씩 당겨지게 됨
    
    while idx >= len(num_list):
        idx -= len(num_list)
    
    answer.append(str(num_list.pop(idx))) # 제거하고 answer 에 값 추가

print(f'<{", ".join(answer)}>')