n, m = map(int, input().split())

graph = []
cnt = 0

for i in range(n):
    graph.append(list(map(int, input())))
print(graph)
#[[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
def dfs(i, j):
    if i<0 or i>=n or j<0 or j>=m:
        return 0
    
    if graph[i][j] == 0:
        graph[i][j] = 1
        
        dfs(i-1 ,j)
        dfs(i, j-1)
        dfs(i+1, j)
        dfs(i, j+1)
        
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i, j)==True:
            cnt+=1
            
print(cnt)