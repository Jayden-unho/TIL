def solution(absolutes, signs):
    my_sum = 0
    for idx in range(len(absolutes)):
        if signs[idx] == False:
            absolutes[idx] = absolutes[idx] * -1

        my_sum += absolutes[idx]

    return my_sum

print(solution([4, 7, 12], [True, False, True]))
print(solution([1, 2, 3], [False, False, True]))