testCase = int(input())

for i in range(1, testCase+1):
    command = int(input())

    speed = 0
    distance = 0

    for _ in range(command):
        cmd = input().rstrip()

        if cmd != '0':
            acc = int(cmd[-1])
        cmd = int(cmd[0])
        
        # 가속인 경우
        if cmd == 1:
            speed += acc

        # 감속인 경우
        elif cmd == 2:
            speed -= acc
            # 속도가 0보다 작아질 경우, 0으로 설정
            if speed < 0:
                speed = 0
        
        distance += speed
    
    print(f'#{i} {distance}')