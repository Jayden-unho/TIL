'''
# 이항계수 n,k -> nCk
# math 모듈 이용. comb - combination 메서드 있음
import sys
import math



n,k = map(int, sys.stdin.readline().split())

answer = math.comb(n,k)
print(answer)
'''



# 반복문 이용한 구현
import sys



n,k = map(int, sys.stdin.readline().split())

answer = 1

# nCk -> n! / (k!*(n-k)!)
# 반복문을 이용하여 진행시, 특정 경우에 무리수가 나와서 오차가 발생
for i in range(1,n+1):
    answer *= i

    if i<=k:
        answer /= i
    if i<=(n-k):
        answer /= i

# 강제로 int로 형변환시에 소수점 뒤의 숫자들은 모두 버림을 하게 되는데
# 위에서 언급한 무리수의 오차가 0.00000001 이라도 발생시 정답에 비해 0.0000000001 이 부족한 현상이 발생
# 예를 들어 10 C 6 의 경우 정답이 210이나 반복문 이용시 209.99~7 와 같은 형태가 발생하게 됨
# 따라서 int로 형변환시 뒤의 숫자들을 모두 버려 210이 아닌 209 발생 <- 반올림의 방법으로 해결 필요
int_answer = int(answer)

if answer - int_answer == 0:
    print(int_answer)    
elif answer - int_answer < 0.5:
    print(int_answer)
elif answer - int_answer > 0.5:
    print(int_answer+1)