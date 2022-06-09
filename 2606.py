computer = int(input())
connected = int(input())
graph=[[]*computer for _ in range(computer+1)]
visited = [0]*(computer+1)
cnt = 0

for i in range(connected):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    visited[start] = 1
    global cnt
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            cnt+=1

dfs(1)
print(cnt)
#[[2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]     
