import sys

s = sys.stdin.readline().lstrip().rstrip().upper()
s_list = []
s_set = []
sign = ''
count = 0

for i in range(len(s)):
    s_list.append(s[i])
s_set = list(set(s_list))

for j in range(len(s_set)):
    if count == s_list.count(s_set[j]):
        count = s_list.count(s_set[j])
        sign = ''
    elif count < s_list.count(s_set[j]):
        count = s_list.count(s_set[j])
        sign = s_set[j]

if count == 0 or sign == '':
    print('?')
else:
    print(sign)