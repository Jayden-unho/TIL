import sys

testCase = int(sys.stdin.readline())

for _ in range(testCase):
    number, target = map(int, sys.stdin.readline().split())
    importance_list = list(enumerate(map(int, sys.stdin.readline().split()) ,start=0))

    answer = []
    
    # 찾고자하는 순서가 들어가면 반복 종료
    while target not in answer:
        high_importance = 0
        idx = -1

        # 목록에서 가장 중요도가 높은 문서의 인덱스 값을 찾아온다
        for i in range(len(importance_list)):
            if high_importance < importance_list[i][1]:
                high_importance = importance_list[i][1]
                idx = i

         
        
        # 맨 앞에 문서가 아니라면
        if idx != 0:    
            importance_list.append(importance_list.pop(0))
        else:
            answer.append(importance_list.pop(0)[0])
    
    print(len(answer))