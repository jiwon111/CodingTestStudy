n, m = map(int, input().split())
a, b, d = map(int, input().split())

total = []
cnt = 1

for _ in range(n):
    M = list(map(int, input().split()))
    total.append(M)

while 1:
    if total[a-1][b]==1 and total[a+1][b]==1 and total[a][b-1] == 1 and total[a][b+1] == 1:
        break
    if d==0:
        if total[a-1][b] == 0:
            total[a-1][b] = 1#가본 칸
            a-=1
            cnt+=1
        else:
            d=3
            continue
    if d==3:
        if total[a][b+1] == 0:
            total[a][b+1] = 1
            b+=1
            cnt+=1
        else:
            d=2
            continue
    if d==2:
        if total[a+1][b] == 0:
            total[a+1][b] = 1
            a+=1
            cnt+=1
        else:
            d = 1
            continue
    if d==1:
        if total[a][b-1] == 0:
            total[a][b-1] = 1
            b-=1
            cnt+=1
        else:
            d=0
    
print(cnt)