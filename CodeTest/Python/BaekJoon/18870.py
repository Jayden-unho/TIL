'''
방법 1 - 리스트의 각 요소들을 접근 -> 리스트의 모든값들과 비교하여 조건에 해당하는게 몇개인지 카운트 - O(N^2)
방법 2 - 리스트를 정렬하여 다른 변수에 저장 -> 리스트 각 요소 접근 -> 정렬된 리스트에서 제일 처음 나오는 인덱스가 몇인지 확인하여 값 반환 - O(NlogN + N)
'''


import sys


n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
sorted_list = sorted(list(set(n_list)), reverse=True)   # 요소보다 작은 값이 필요하고, 스택 pop 이용하므로 내림차순 정렬
count = {}

cnt = 0
while sorted_list:                                      # 내림차순으로 정렬된 리스트를 맨뒤에서 하나씩 꺼내서 딕셔너리에 값 저장
    count[sorted_list.pop()] = cnt
    cnt += 1

for e in n_list:                                        # 요소별로 갯수 출력
    print(count.get(e), end=' ')