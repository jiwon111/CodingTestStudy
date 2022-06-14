from collections import deque

n, k = map(int, input().split())
visited = [0]*(100000+1)

def bfs(n, k):
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        dx = [x-1, x+1, x*2]
        if x == k:
            print(visited[x])
            break
        for i in dx:
            if 0<=i<=100000 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[x]+1
bfs(n, k)