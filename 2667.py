n = int(input())
cnt = 0
graph = []
total_house=[]
house=0
for i in range(n):
    graph.append(list(map(int, input())))
    
print(graph)

def dfs(i, j):
    if i<0 or j<0 or i>=n or j>=n:
        return False
    
    if graph[i][j] == 1:
        print(house)
        house+=1
        graph[i][j] = 0
        
        dfs(i-1 ,j)
        dfs(i, j-1)
        dfs(i+1, j)
        dfs(i, j+1)
        total_house.append(house)
        return True
    return False

for i in range(n):
    for j in range(n):
        house=0
        if dfs(i, j) == True:
            cnt+=1

print(cnt)
print(total_house)