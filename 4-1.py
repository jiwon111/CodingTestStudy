n=int(input())
move = list(map(str, input().split()))
start=[1, 1]
for m in move:
        if m=='R' and start[1]<n:
            start[1]+=1
        elif m=='U' and start[0]>1:
            start[0]-=1
        elif m=='L' and start[1]>1:
            start[1]-=1
        elif m=='D' and start[0]<n:
            start[0]+=1
print(start)