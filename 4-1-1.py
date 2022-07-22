n=int(input())
plan = list(map(str, input().split()))
dx=[0, 0, -1, 1]
dy=[-1, 1, 0, 0]
p=['u', 'd', 'l', 'r']
x, y = 1, 1

for i in range(len(plan)):
    for j in range(len(p)):
        if plan[i] == p[j]:
            nx = x+dx[j]
            ny = y+dy[j]
            print(nx, ny)
    if nx<1 or nx>n or ny<1 or ny>n:
        continue
    x, y = nx, ny
print(y, x)