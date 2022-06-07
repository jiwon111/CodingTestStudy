from collections import deque

queue = deque()

def bfs(graph, v, visited):
    queue.append(v)
    visited[v] = 1
    
    while queue:
        pop = queue.popleft()
        print(pop, end=' ')
        
        for i in graph[pop]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
    
            
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited = [0]*9

bfs(graph, 1, visited)