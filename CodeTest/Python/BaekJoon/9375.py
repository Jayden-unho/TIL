import sys



test_case = int(sys.stdin.readline())

for _ in range(test_case):
    num = int(sys.stdin.readline())
    wear_dict = {}
    answer = 1

    # 항목들 딕셔너리에 저장
    for _ in range(num):
        name, kind = sys.stdin.readline().strip().split()
        wear_dict[kind] = wear_dict.get(kind, []) + [name]
    
    for k, v in wear_dict.items():
        answer *= len(v)+1
    
    print(answer-1)