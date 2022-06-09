import sys
sys.setrecursionlimit(10000)#런타임 에러(RecursionError)

t = int(input())#테스트 케이스

def dfs(i, j):
    if i<0 or j<0 or i>=n or j>=m:
        return False
    if graph[i][j] == 1:
        graph[i][j] = 0

        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)

        return True
    return False 

for _ in range(t):
    m, n, k = map(int, input().split())#가로, 세로
    graph = [[0]*m for _ in range(n)]
    cnt = 0


    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            if dfs(i, j)==True:
                cnt+=1
    print(cnt)