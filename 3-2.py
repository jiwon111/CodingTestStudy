n, m, k = map(int, input().split())
data=list(map(int, input().split()))

data.sort()#정렬
max1=data[n-1]
max2=data[n-2]
total = 0
while 1:
    if m==0:
        break
    total+=max1*k
    total+=max2
    m=m-k-1
    
print(total)