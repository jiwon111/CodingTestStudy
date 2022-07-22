n, m = map(int, input().split())
cards=[]
m=[]
for i in range(n):
    card=list(map(int, input().split()))
    m.append(min(card))
print(max(m))
    