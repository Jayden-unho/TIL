def solution(n, k, cmds):
    answer = []                         # 행 삭제 여부를 저장할 정답 리스트
    history = []                        # 삭제된 행이 저장될 스택
    table = []                          # 연결 리스트

    def create_item(idx):               # 연결 리스트 초기 생성
        item = [[idx-1, -1], idx]       # [이전 인덱스, 이후 인덱스], 현재 인덱스(데이터)
        if idx != 0:                    # 가장 앞의 인덱스가 아닌 경우에만, 앞의 리스트의 이후 인덱스 값을 현재 인덱스로 지정
            table[idx-1][0][1] = idx
        return item

    def forward_idx(num):               # 연결 리스트 앞으로 이동
        nonlocal k

        for _ in range(num):            # 숫자만큼 위로 이동
            if table[k][0][0] == -1:    # 가장 앞인 경우 더 이상 이동 불가
                return
            k = table[k][0][0]          # 앞의 인덱스로 이동

    def backward_idx(num):              # 연결 리스트 뒤로 이동
        nonlocal k

        for _ in range(num):            # 숫자만큼 뒤로 이동
            if table[k][0][1] == -1:    # 가장 뒤인 경우 더 이상 이동 불가
                return
            k = table[k][0][1]          # 뒤의 인덱스로 이동

    def delete_row():                           # 표의 행 삭제
        nonlocal k

        pre_idx = table[k][0][0]                # 이전 인덱스의 값
        after_idx = table[k][0][1]              # 이후 인덱스의 값

        history.append(k)                       # 삭제한 행 목록에 기록
        if pre_idx != -1:                       # 가장 앞의 리스트가 아니면
            table[pre_idx][0][1] = after_idx    # 앞의 인덱스를 뒤의 인덱스로 연결
        if after_idx != -1:                     # 가장 뒤의 리스트가 아니면
            table[after_idx][0][0] = pre_idx    # 뒤의 인덱스를 앞의 인덱스로 연결
        
        if after_idx == -1:     # 가장 뒤의 인덱스가 삭제되면, 인덱스 한칸 앞으로 이동
            k = pre_idx
        else:                   # 그 외, 인덱스 한칸 뒤로 이동
            k = after_idx

    def recovery():                             # 삭제된 행 복구
        nonlocal k

        item = table[history.pop()]             # 마지막에 삭제한 행을 꺼냄

        pre_idx = item[0][0]                    # 앞의 인덱스와 뒤의 인덱스의 값
        after_idx = item[0][1]

        if pre_idx != -1:                       # 원래 자리에 다시 연결
            table[pre_idx][0][1] = item[1]
        if after_idx != -1:
            table[after_idx][0][0] = item[1]

    for idx in range(n):                    # 초기에 개수만큼 이중연결 리스트 생성
        table.append(create_item(idx))

    for cmd in cmds:
        cmd = cmd.split(' ')
        
        if cmd[0] == 'U':               # 인덱스 위로 이동
            forward_idx(int(cmd[1]))
        elif cmd[0] == 'D':             # 인덱스 아래로 이동
            backward_idx(int(cmd[1]))
        elif cmd[0] == 'C':             # 행 삭제
            delete_row()
        elif cmd[0] == 'Z':             # 삭제한 행 복구
            recovery()

    history = set(history)              # 삭제된 행의 인덱스 목록을 집합화 시킴
    for i in range(n):
        if i not in history:            # 삭제된 목록에 없으면, 변화 없으므로 O
            answer.append('O')
        else:                           # 삭제된 목록에 있으면, 변화 있으므로 X
            answer.append('X')

    return ''.join(answer)

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))