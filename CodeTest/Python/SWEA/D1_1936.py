# 가위 - 1, 바위 - 2, 보 - 3
a, b = map(int, input().split())

if a != 3:
    if a-b > 0:
        print('A')
    else:
        print('B')
else:
    if a-b == 1:
        print('A')
    else:
        print('B')