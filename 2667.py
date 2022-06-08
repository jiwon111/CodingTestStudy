n = int(input())
cnt = 0
graph = []
house = []
for _ in range(n):
    graph.append(list(map(int, input())))

house_cnt=0
def dfs(i, j, house):
    global house_cnt
    if i<0 or j<0 or i>=n or j>=n:
        return False
    if graph[i][j]==1:
        house_cnt+=1
        graph[i][j] = 0
        dfs(i, j+1, house)
        dfs(i, j-1, house)
        dfs(i-1, j, house)
        dfs(i+1, j, house)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j, house):
            cnt+=1
            house.append(house_cnt)
            house_cnt=0

print(cnt)
house.sort()
for i in house:
    print(i)