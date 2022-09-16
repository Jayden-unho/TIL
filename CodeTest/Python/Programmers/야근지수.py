def solution(n: int, works: list[int]) -> int:
    answer = 0
    sorted_works = sorted(works)
    stack = []

    while n > 0:
        stack_length = len(stack)

        if not stack and not sorted_works:
            break
        elif not stack:
            stack.append(sorted_works.pop())
            continue
        elif sorted_works:
            w = sorted_works[-1]
            s = stack[-1]

            if w == s:
                stack.append(sorted_works.pop())
                continue

            diff = s - w
            if n >= diff * stack_length:
                n -= diff * stack_length
                sorted_works.extend([w] * stack_length)
                stack.clear()
                continue

        div = n // stack_length
        remain = n % stack_length
        n = 0

        for k in range(stack_length):
            stack[k] -= div
            if remain:
                stack[k] -= 1
                remain -= 1

    while stack:
        s = stack.pop()
        if s > 0:
            answer += s ** 2

    while sorted_works:
        s = sorted_works.pop()
        if s > 0:
            answer += s ** 2

    return answer


print(solution(4, [4, 3, 3, ]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))
