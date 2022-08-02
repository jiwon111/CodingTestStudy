from itertools import combinations

n, m = map(int, input().split())
ball=list(map(int, input().split()))
cnt=0
c = list(combinations(ball, 2))
for i in range(len(c)):
    if c[i][0]!=c[i][1]:
        cnt+=1
print(cnt)