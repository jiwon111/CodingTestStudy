def solution(periods, payments, estimates):
    answer = []
    vip = 0
    nvip = 0
    client = len(periods)
    total = []
    isVip=[0]*client
    estimate = []
    total2 = []

    for i in range(client):
        total.append(sum(payments[i]))

#지금 vip냐?
    for i in range(client):
        if periods[i]<60 and periods[i]>=24 and total[i]>=900000:
            isVip[i]+=1
        elif periods[i]>=60 and total>=600000:
            isVip+=1

    for i in range(client):
        for j in range(len(estimates)):
            payments[i][j] = estimates[i]

    for i in range(client):
        total.append(sum(payments[i]))

#지금 vip아닌데 앞으로 될 사람
    for i in range(client):
        if isVip[i]==0:
            if total[i]>=900000 and periods[i]+1>=24:
                vip+=1
            elif periods[i]+1>=60 and total[i]>=600000:
                vip+=1
        else:
            if periods[i]+1<60 and periods[i]+1>=24 and total[i]<900000:
                nvip+=1
            elif total[i]<600000:
                nvip+=1
    answer.append(vip)
    answer.append(nvip)
    return answer

periods = [20, 23, 24]
payments = [[100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000]
, [100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000],
[350000, 50000, 50000,50000,50000,50000,50000,50000,50000,50000,50000,50000]]
estimates = [100000, 100000, 100000]
solution(periods, payments, estimates)