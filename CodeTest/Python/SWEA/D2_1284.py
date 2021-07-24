testCase = int(input())

for i in range(1, testCase+1):
    '''
    water1 - A회사 l당 요금
    water2_default - B회사 기준점 이하시 기본요금
    water2_line - B회사 기준점
    water2_plus - B회사 l당 추가요금
    use_water - 물 사용량
    '''
    water1, water2_default, water2_line, water2_plus, use_water = map(int, input().split())

    # A회사 요금
    water1_total = water1 * use_water

    # B회사 요금
    # 기준 이하시
    if use_water <= water2_line:
        water2_total = water2_default
    # 기준 초과시
    else:
        water2_total = water2_default + ((use_water-water2_line)*water2_plus)

    if water1_total < water2_total:
        print(f'#{i} {water1_total}')
    else:
        print(f'#{i} {water2_total}')