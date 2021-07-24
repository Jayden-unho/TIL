MONTH_DAY = {
    '01':31,
    '02':28,
    '03':31,
    '04':30,
    '05':31,
    '06':30,
    '07':31,
    '08':31,
    '09':30,
    '10':31,
    '11':30,
    '12':31
}

testCase = int(input())

for i in range(1, testCase+1):
    num = input().rstrip()
    
    year = num[:4]
    month = num[4:6]
    day = num[6:]

    if int(month)<1 or int(month)>12:
        year = '-1'

    if year != '-1' and MONTH_DAY[month] < int(day):
        year = '-1'

    if year == '-1':
        print(f'#{i} -1')
    else:
        print(f'#{i} {year}/{month}/{day}')