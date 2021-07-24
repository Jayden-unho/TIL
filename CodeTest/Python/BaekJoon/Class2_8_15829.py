import sys



l = int(sys.stdin.readline().rstrip())
input_str = sys.stdin.readline().rstrip()

answer = 0
M = 1234567891

# 아스키코드 값 a-97 / z-122
for i in range(len(input_str)):
    answer += (ord(input_str[i]) - 96)*31**i

print(answer%M)