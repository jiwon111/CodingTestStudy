def solution(N, stages):
    answer = []
    fail = [] #실패율
    print(N)
    for i in range(N):
        #i+1 스테이지
        n = stages.count(i+1) # 몇명이 멈춰있는지
        total = 0
        for j in stages:
            if j>=i+1:
                total+=1
        if total!=0:
            fail.append((i+1, n/total))
        else:
            fail.append((i+1, n/len(stages)))
    fail.sort(key=lambda x:x[1], reverse = True)
    print(fail)
    for i in range(len(fail)):
        answer.append(fail[i][0])
    print(answer)
    return answer
#5, [3,3,3,3]
N=5
stages = [3, 3, 3, 3]
solution(N, stages)