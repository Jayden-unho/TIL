'''
가로가 작든 세로가 작든 답은 동일
예를 들어 가로가 더 작은 경우
가로 1칸에 세로가 어느정도 길이인지 구함 -> 5,12 일때 (1, 12/5), (2, 12/5*2), (3, 12/5*3) ....
1칸에서 정수의 범위를 넘은 소수이면 올림을 한다. 예를 들어 1칸에 1.7의 길이라면 대각선이 차지하는 공간은 2칸을 차지하게 된다.
그 다음칸에서 생각할때는 (2, 3.4) 라면 현재 y좌표의 3.4를 올림하여 4가 되고 이전에 1.7에서 내림을 한 1을 빼면 2번째칸에서 잘리는 공간들이다. -> 반복
만약 끝점이 10, 12 라면 모두 반복하면 시간이 오래 걸림 그래서 저기의 이전 지점인 5,6 까지만 경우를 구하고 남은 부분은 곱을 하여 구한다.
위의 방법을 구하는건 y 좌표를 x 좌표로 나눌때 y 좌표가 정수가 된다면 그만하면 된다.
'''
import math



def solution(w, h):
    total = w * h       # 사용 가능한 정사각형 갯수
    disable = 0         # 사용 불가능한 정사각형 갯수
    coordinate = []
    pre, after = 0, 0

    if w > h:           # 더 짧은 길이를 w에 두기 위함, 크게 상관은 없으나 값 차이가 커지는 경우 반복을 줄일 수 있다.
        w, h = h, w
    
    mul = 1
    while mul == 1 or not float(h/w * (mul-1)).is_integer():  # w 값이 1일때마다의 h의 값들을 리스트로 담아냄, 결과가 정수가 아니면 반복
        coordinate.append([mul, h/w*mul])
        mul += 1

    # print(coordinate)
    for e in coordinate:
        after = int(math.ceil(e[1]))
        disable += after - pre
        pre = after - 1
    
    if e[0] != w:
        disable *= w//e[0]
    
    answer = total - disable
    return answer


print(solution(8, 12))
print(solution(10, 10))
print(solution(1, 10))
print(solution(5, 5))
print(solution(50, 50))