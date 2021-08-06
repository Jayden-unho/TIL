COORDINATE = {
    1 : [0, 0],
    2 : [0, 1],
    3 : [0, 2],
    4 : [1, 0],
    5 : [1, 1],
    6 : [1, 2],
    7 : [2, 0],
    8 : [2, 1],
    9 : [2, 2],
    0 : [3, 1],
}

def solution(numbers, hand):
    answer = ''
    left_now = [3,0]
    right_now = [3,2]

    for number in numbers:
        # 왼손으로만
        if number%3 == 1:
            answer += 'L'
            left_now = COORDINATE[number]
        # 오른손으로만
        elif number%3 == 0 and number != 0:
            answer += 'R'
            right_now = COORDINATE[number]
        # 양손 중 선택
        else:
            left_distance = abs(left_now[0] - COORDINATE[number][0]) + abs(left_now[1] - COORDINATE[number][1])     # 왼손 거리
            right_distance = abs(right_now[0] - COORDINATE[number][0]) + abs(right_now[1] - COORDINATE[number][1])  # 오른손 거리
            
            # 거리 비교
            if left_distance < right_distance:
                answer += 'L'
                left_now = COORDINATE[number]
            elif left_distance > right_distance:
                answer += 'R'
                right_now = COORDINATE[number]
            else:
                if hand == 'right':
                    answer += 'R'
                    right_now = COORDINATE[number]
                else:
                    answer += 'L'
                    left_now = COORDINATE[number]



    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))