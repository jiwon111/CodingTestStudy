n = int(input())
cnt = 0
graph = []
house = []
global house_cnt
for _ in range(n):
    graph.append(list(map(int, input())))
print(graph)

house_cnt=0
def dfs(i, j, house, house_cnt):
    if i<0 or j<0 or i>=n or j>=n:
        return False
    if graph[i][j]==1:
        graph[i][j] = 0

        dfs(i, j+1, house, house_cnt)
        dfs(i, j-1, house, house_cnt)
        dfs(i-1, j, house, house_cnt)
        dfs(i+1, j, house, house_cnt)
        house_cnt+=1
        print('house_cnt=', house_cnt)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j, house, house_cnt):
            cnt+=1
            print('여기', house_cnt)
            house.append(house_cnt)
            house_cnt=0


print(cnt)
print(house)