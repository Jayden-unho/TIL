def to_binary(comb_arr):
    result = []
    
    for elements in comb_arr:
        tmp_list = []
        for e in elements:
            tmp = ''    
            while e:
                tmp = str(e%2) + tmp
                e //= 2
            if tmp == '':
                tmp = '0'
            tmp_list.append(tmp)
        result.append(tmp_list)    
    
    return result

def solution(n, arr1, arr2):
    answer = []

    comb_arr = list(zip(arr1, arr2))
    binary_list = to_binary(comb_arr)

    for e in binary_list:
        my_sum = str(int(e[0]) + int(e[1]))

        while len(my_sum) < n:
            my_sum = '0' + my_sum

        my_sum = my_sum.replace('0', ' ').replace('2', '#').replace('1', '#')
        answer.append(my_sum)

    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))
print(solution(1, [1], [0]))