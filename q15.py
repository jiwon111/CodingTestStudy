from collections import deque

n, m, k, x = map(int, input().split())
graph = [[]*n for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
print(graph)

def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            visited[i] = visited[v]+1
            queue.append(i)
flag = 0
bfs(x)
for i in range(1, n+1):
    if visited[i] == k:
        print(i)
        flag = 1

if flag == 0:
    print(-1)