from collections import deque

n, m, v = map(int, input().split())
visited_dfs = [0]*(n+1)
visited_bfs = [0]*(n+1)

graph = [[]*n for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

#작은 노드부터 방문해야해서 그래프 정렬
for i in range(len(graph)):
    graph[i].sort()
    
def dfs(v):
    visited_dfs[v] = 1
    print(v, end=' ')
    for i in graph[v]:
        if visited_dfs[i] == 0:
            dfs(i)
            
def bfs(v):
    queue = deque()
    queue.append(v)
    visited_bfs[v] = 1
    
    while queue:
        p = queue.popleft()
        print(p, end=' ')
        
        for i in graph[p]:
            if visited_bfs[i] == 0:
                visited_bfs[i] = 1
                queue.append(i)
                
dfs(v)
print()
bfs(v)