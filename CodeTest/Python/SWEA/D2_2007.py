testCase = int(input())
answer = ''


for i in range(1, testCase+1):
    pattern = input()

    # 슬라이싱을 이용해서 패턴의 0번부터 글자 하나를 늘리며 마디를 찾는다
    for j in range(1, len(pattern)+1):
        answer = pattern[0:j]

        compare = answer*((len(pattern)//len(answer)) + 1)
        compare = compare[:len(pattern)]

        # 마디를 찾았을때
        if compare == pattern:
            break
    
    print(f'#{i} {len(answer)}')
