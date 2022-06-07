from collections import deque

queue = deque()

n, m = map(int, input().split())
graph=[]

#dx+dy = [상, 하, 좌, 우]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph.append(list(map(int, input())))
    
def bfs(x, y):
    queue.append((x, y))
    
    while queue:
        pop_x, pop_y = queue.popleft()
        
        for i in range(4):
            if pop_x+dx[i]<0 or pop_x+dx[i]>=n or pop_y+dy[i]<0 or pop_y+dy[i]>=m:
                continue
            if graph[pop_x+dx[i]][pop_y+dy[i]] == 0:
                continue
            if graph[pop_x+dx[i]][pop_y+dy[i]] == 1:
                graph[pop_x+dx[i]][pop_y+dy[i]]=graph[pop_x][pop_y]+1
                queue.append((pop_x+dx[i], pop_y+dy[i]))
    print(graph[n-1][m-1])
    
bfs(0, 0)