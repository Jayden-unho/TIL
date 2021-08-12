import sys



num = int(sys.stdin.readline())
meet_list = [list(map(int, sys.stdin.readline().split())) for _ in range(num)]


meet_list.sort(key=lambda x: (x[1], x[0]))
end_time = 0
cnt = 0

for e in meet_list:
    if e[0] >= end_time:
        end_time = e[1]
        cnt += 1

print(cnt)