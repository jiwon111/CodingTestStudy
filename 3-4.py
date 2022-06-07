cnt = 0
n, k = map(int, input().split())

while 1:
    if n==1:
        break
    if n%k==0:
        n=n//k
        cnt+=1
    else:
        n=n-1
        cnt+=1
        
print(cnt)