from math import log2


def get_binary(num):
    binary = bin(num)[2:]
    length = len(binary)
    h = log2(length + 1)

    if h == int(h):
        return binary, length
    result = '0' * (2**(int(h)+1) - 1 - length) + binary
    return result, len(result)


def sol(num, left, right):
    if left == right:
        return int(num[left])

    mid = (left + right) // 2
    l = sol(num, left, mid-1)
    r = sol(num, mid+1, right)

    if l == -1 or r == -1:  # 왼쪽/오른쪽 서브트리 중 하나라도 유효하지 않으면
        return -1
    elif l or r:            # 왼쪽/오른쪽 서브트리 중 노드가 존재하면
        if num[mid] == '1':  # 부모노드가 존재하면
            return 1        # 노드 존재(정상)
        return -1           # 유효하지 않음
    elif num[mid] == '1':   # 부모노드만 존재하면
        return 1
    return 0


def solution(numbers):
    answer = []

    for num in numbers:
        binary, length = get_binary(num)
        if sol(binary, 0, length-1) == -1:
            answer.append(0)
        else:
            answer.append(1)

    return answer


print(solution([511, 512]))
print(solution([63, 111, 95, 255]))
