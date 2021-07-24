def set_DECODING_TABLE():
    '''
    dict 형태의 디코딩 테이블 생성
    '''
    
    for x in range(26):
        key_upper = chr(x+65)
        key_lower = chr(x+97)

        DECODING_TABLE[key_upper] = x
        DECODING_TABLE[key_lower] = x+26

    for x in range(10):
        DECODING_TABLE[str(x)] = x+52

    DECODING_TABLE['+'] = 62
    DECODING_TABLE['/'] = 63

def decimal_to_binary(num):
    '''
    10진수를 2진수로 변경 (문자열로 반환)
    '''
    answer = ''
    
    while num > 0:
        answer = str(num%2) + answer
        num //= 2

    # 6비트가 아니면 앞에 0을 붙여줌
    while len(answer) != 6:
        answer = '0' + answer
    
    return answer

def binary_to_decimal(binaryNum):
    answer = 0
    i = 0

    while binaryNum:
        num = int(binaryNum[-1])
        if num == 1:
            answer += 2**i

        binaryNum = binaryNum[:-1]
        i += 1

    return answer


def redivide():
    '''
    디코딩 된 6비트 2진수들을 4개를 합치고, 다시 3등분으로 나누어서 저장하는 함수
    '''
    tmp_list = [] # 2진수들 4개를 합친걸 임시적으로 담아두는 리스트

    # 2진수 4개를 이어붙여서 tmp_list에 저장
    for i in range(0, len(decoding_list), 4):
        tmp = ''
        for j in range(i, i+4):
            tmp += decoding_list[j]
        tmp_list.append(tmp)

    # 24비트를 8비트 3개로 나눠서 담음
    for i in range(len(tmp_list)):
        for j in range(3):
            redivide_list.append(tmp_list[i][j*8:j*8+8])



DECODING_TABLE = {}
set_DECODING_TABLE()

testCase = int(input())

for index in range(1, testCase+1):
    in_str = input().strip()
    decoding_list = [] # 디코딩 되어 2진법으로 변형된 값들을 담는 리스트 변수
    redivide_list = [] # 디코딩 된 6비트 2진수를 8비트로 변형하여 담는 리스트 함수
    answer_list = []   # 정답 숫자를 담는 리스트 변수

    # 디코딩 후 2진법으로 변형하여 리스트에 저장
    while in_str:
        decoding_list.append(decimal_to_binary(DECODING_TABLE[in_str[0]]))
        in_str = in_str[1:]

    # 2진수 재배치    
    redivide()
    
    # 2진수를 10진수 값으로 변경
    for binaryNum in redivide_list:
        answer_list.append(binary_to_decimal(binaryNum))

    print(f'#{index}', end=' ')
    for c in answer_list:
        print(chr(c), end='')
    print()