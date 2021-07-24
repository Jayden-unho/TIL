import sys
import datetime # 코드 소요 시간 측정하기 위함



# 코드 시작시 시간 측정
start_time = datetime.datetime.now()

up, down, high = map(int, sys.stdin.readline().split())

# high-up -> 며칠간의 반복 후 어떠한 값이 되었고, up을 한번 진행하면 high를 0보다 작거나 같은 수를 만드는 경우를 구한다
# up-down 이 high-up보다 크거나 같아지는 경우
# (up-down)*i >= high-up
# i >= (high-up) / (up-down)
day = (high-up)//(up-down)
sign = (high-up)%(up-down)  # up을 했을때, 딱 0이 나오면 1회 늘고, 딱 맞지 않으면 2회 추가

if sign == 0: print(day+1)
elif sign != 0: print(day+2)


# 코드 종료 후 시간 측정
end_time = datetime.datetime.now()
# seconds 사용해서 초를 구할수 있지만, 정수형 리턴으로 자세한 시간을 구하려면 아래 방식 사용
print((end_time - start_time).microseconds/1000/1000,'초')

"""
# 극단적인 경우 실행 시간이 너무 오래걸림
# 빅오를 더 낮춰야함
day = 0

while high >= 0:
    day += 1

    high -= up

    if high<=0:
        break
    else:
        high += down
print(day)
"""