import sys
sys.stdin = open('input.txt')


# 가장 나중에 사용되거나 앞으로 사용하지 않을 숫자 반환
def get_far_num(arr):
    idxs = {}

    for p in plug:
        if p not in arr:
            return p
        else:
            k = arr.index(p)
            idxs[k] = p

    max_key = max(idxs.keys())
    return idxs[max_key]


# 입력 데이터
N, K = map(int, sys.stdin.readline().split())
li = list(map(lambda x: int(x)-1, sys.stdin.readline().split()))

answer = 0

# 플러그 꽂아진 숫자들
plug = set()
for idx in range(K):
    # 다음에 사용할 번호
    next = li[idx]

    # 이미 플러그에 꽂아서 사용중이면 아무 동작 안함
    if next in plug:
        pass
    # 플러그 모두 사용중 아니라면 추가
    elif len(plug) < N:
        plug.add(next)
    # 가장 나중에 사용되거나 앞으로 사용되지 않을 숫자 삭제 및 새로 추가
    else:
        num = get_far_num(li[idx+1:])
        plug.remove(num)
        plug.add(next)
        answer += 1


print(answer)
