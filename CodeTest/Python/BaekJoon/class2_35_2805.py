import sys


def calc(mid, *trees):
    answer = 0

    for tree in trees:
        if tree > mid:
            answer += (tree - mid)

    return answer

num, target = map(int, sys.stdin.readline().split())
tree_list = list(map(int, sys.stdin.readline().split()))

# 가장 많은 나무 길이를 가져가기 위한 높이 설정 : high
# 가장 적은 나무 길이를 가져가기 위한 높이 설정 : low
high = max(tree_list)-1     # 나무를 최소 1 이상 가져가야하므로 -1 설정
low = 0


while low <= high:
    mid = (high+low)//2
    total = 0

    # list comprehension 이 일반 반복문 보다 수행 시간이 조금 더 빠름
    total = sum([tree-mid for tree in tree_list if tree>mid])
    
    if total >= target:
        low = mid + 1
        answer = mid
    elif total <= target:
        high = mid - 1

print(answer)