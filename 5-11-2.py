from collections import deque

n, m = map(int, input().split())
#상 하 좌 우
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
graph=[]
#[[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
for _ in range(n):
    graph.append(list(map(int, input())))
print(graph)

def bfs(i, j):
    queue=deque()
    
    queue.append((i, j))
    while queue:
        i, j = queue.popleft()
        
        for i in range(4):
            nx = i+dx[i]
            ny = j+dy[i]
            
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[i][j]+1
                queue.append((nx, ny))
                
    return graph[n-1][m-1]