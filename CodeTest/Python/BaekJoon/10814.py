import sys

number = int(sys.stdin.readline())
member_list = []

# 가입순서대로 정보가 들어오므로 가입순서에 해당하는 인덱스 S 를 사용
for s in range(number):
    member_list.append(list(sys.stdin.readline().split()))
    member_list[s].append(int(s))

member_list = sorted(member_list, key=lambda member_list: (int(member_list[0]), member_list[2]), reverse=True)

while member_list:
    member = member_list.pop()
    print(member[0], member[1])