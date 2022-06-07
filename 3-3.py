n, m = map(int, input().split())
card=[0 for _ in range(n)]
result = 0
for i in range(n):
    card[i]=list(map(int, input().split()))
    Min = min(card[i])
    result = max(result, Min)

print(result)