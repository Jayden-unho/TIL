import sys
sys.stdin = open('input.txt', 'r')

testCase = int(input())

for index in range(1, testCase+1):
    days = int(input())
    prices = list(reversed(list(map(int, input().split()))))
    #prices.reversed()
    benefit = 0

    max_price = max(prices)
    while prices:
        now_price = prices.pop()   # 현재 가격 가져오고 리스트에서 제거

        if now_price == max_price:  # 현재 가격과 최고가를 비교
            if not prices:          # 가격들이 비어있다면 종료
                break
            max_price = max(prices)
            continue
        
        benefit += max_price - now_price

    print(f'#{index} {benefit}')