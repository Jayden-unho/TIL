import sys



test_case = int(sys.stdin.readline())

for _ in range(test_case):
    num = int(sys.stdin.readline())
    wear_dict = {}

    # 항목들 딕셔너리에 저장
    for _ in range(num):
        name, kind = sys.stdin.readline().strip().split()
        wear_dict[kind] = wear_dict.get(kind, []) + [name]
    
    