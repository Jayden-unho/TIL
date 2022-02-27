def solution(n, k):
    nums = []                   # 진수 변환 후 조건에 맞는 숫자 리스트
    prime_number = {}           # 이미 소수 여부를 확인한 숫자들
    answer = 0                  # 정답

    def trans(num):             # 진수로 변환해주는 함수
        result = 0              # 변환된 숫자
        idx = 0                 # 자릿수

        while num > 0:
            result += (num%k) * (10**idx)       # 나머지값을 결과값의 앞에 추가
            num //= k                           # 몫 저장
            idx += 1                            # 자릿수 증가

        return result                           # 변환된 숫자 반환

    def get_nums(num):                          # 주어진 조건에 해당하는 숫자를 뽑아냄
        tmp, idx = 0, 0                         # 숫자 찾을 임시 변수, 자릿수

        while num > 0:                          # 변환된 수가 아직 남아있으면
            if num % 10:                        # (나머지) 일의 자리가 0이 아닌 숫자라면
                tmp += (num%10) * (10**idx)     # 임시변수에 저장
                idx += 1                        # 자릿수 증가
            else:                               # (나머지) 일의 자리가 0인 경우
                if tmp > 1:                     # 앞에서 저장한 임시변수가 1 보다 크면 숫자 리스트에 추가 (1은 소수가 아니므로 판독할 필요 없음)
                    nums.append(tmp)
                tmp, idx = 0, 0                 # 임시변수와 자릿수 초기화
            num //= 10                          # 10으로 나눈 몫을 재할당
        nums.append(tmp)                        # 임시변수에 값이 남아있으므로 그 수를 숫자 리스트에 저장

    def is_prime(num):                          # 소수 판별
        for i in range(2, int(num**0.5) + 1):   # 제곱근까지만 확인
            if not num % i:                     # 나누어 떨어진다면, 소수가 아님
                prime_number[num] = 0           # 이 숫자를 다음번에 더 판독하지 않기 위해 딕셔너리에 기록
                return 0                        # 0 반환

        prime_number[num] = 1                   # 딕셔너리에 기록
        return 1                                # 1 반환

    transed = trans(n)                          # 주어진 숫자를 k진수로 변환
    get_nums(transed)                           # 변환한 진수에서 주어진 조건에 해당하는 숫자들을 반환

    for num in nums:                            # 각 숫자들을 확인
        if prime_number.get(num, -1) == -1:     # 소수 여부 판독하지 않은 숫자라면
            answer += is_prime(num)             # 판별해서 결과값 더하기
        else:                                   # 이전에 확인한 숫자라면
            answer += prime_number.get(num)     # 기록된 값을 가지고 와서 더하기
    return answer

print(solution(437674, 3))
print(solution(110011, 10))