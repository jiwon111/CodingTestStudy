def solution(n, plans, clients):
    plan = []
    client = []
    answer=[0]*len(clients)
    for p in plans:
        plan.append(list(map(int, p.split(" "))))

    for c in clients:
        client.append(list(map(int, c.split(" "))))

    for i in range(len(client)):
        for j in range(len(plan)):
            if client[i][0]<=plan[j][0]:
                cnt = 1
                for c in range(1, len(client[i])):
                    for p in range(1, len(plan[j])):
                        if client[i][c] == plan[j][p]:
                            if cnt == len(client[i])-2:
                                answer[i]=j+1
                            cnt+=1
    print(answer)
    return answer

#n:부가서비스갯수
n=5
#데이터 추가부가서비스
plans = ["100 1 3", "500 4", "2000 5"]
#이용데이터 이용부가서비스
clients = ["300 3 5", "1500 1", "100 1 3", "50 1 2"]
solution(n, plans, clients)