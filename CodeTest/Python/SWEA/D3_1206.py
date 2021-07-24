import sys
sys.stdin = open('input.txt', 'r')

for index in range(1, 11):
    number = int(input())    
    building_high = list(map(int, input().split()))
    
    answer = 0

    # 방법 1
    # 해당 위치의 왼쪽과 오른쪽 두칸을 비교함
    for i in range(2, number-2):
        tmp1 = tmp2 = tmp3 = tmp4 = 0

        # 값으로 0이 나오면 높이가 같음, 음수가 나오면 옆에 더 큰 빌딩이 있음
        tmp1 = building_high[i] - building_high[i-2]
        tmp2 = building_high[i] - building_high[i-1]
        tmp3 = building_high[i] - building_high[i+1]
        tmp4 = building_high[i] - building_high[i+2]

        # 옆에 가장 큰 빌딩과 높이 차이를 정답에 추가해야함
        if tmp1 > 0 and tmp2 > 0 and tmp3 > 0 and tmp4 > 0:
            answer += min(tmp1, tmp2, tmp3, tmp4)


    print(f'#{index} {answer}')