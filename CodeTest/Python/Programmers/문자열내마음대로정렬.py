'''
1. 문자열이 담긴 리스트를 정렬한다.
2. n번 인덱스에 해당하는 문자를 새로운 리스트에 담는다.
3. 각 문자들을 정렬한다.
4. 문자열을 순환하며 n번째 인덱스에 해당 문자가 있다면 정답 리스트에 추가
5. 한바퀴 돌고나면 다시 반복


* 예상 시간 복잡도 - O(N^2)
문자열 리스트 정렬 - O(N)
인덱스 문자 리스트에 추가 - O(N)
각 문자들 정렬 - O(N)
정렬된 인덱스 문자들 요소 하나씩 가져오며 반복 - O(N)
    문자열 리스트에 한번씩 확인 - O(N)
    문자열 리스트에서 정답 추가 삭제 - O(N)
'''


def solution(strings, n):
    strings.sort()                      # 인덱스가 같은 경우 사전순으로 정렬하기 위해 미리 정렬
    chr_list = []
    answer = []

    for e in strings:                   # 문자열에서 해당 인덱스 문자 리스트에 추가
        chr_list.append(e[n])

    chr_list = list(set(chr_list))      # 문자 중복 제거 
    chr_list.sort()                     # 문자 사전순으로 정렬

    for c in chr_list:
        for e in strings:
            if e[n] == c:
                answer.append(e)

    return answer


print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))
print(solution(['abcd', 'abc', 'abcde'], 2))