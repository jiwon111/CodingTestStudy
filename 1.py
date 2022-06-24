def solution(p):
    j = p.index(min(p))
    n = len(p)
    answer = [0]*n
    for i in range(n):
        j=p.index(min(p))
        if i!=j:
            answer[i]+=1
            answer[j]+=1
            tmp = p[i]
            p[i] = p[j]
            p[j] = tmp
        p[i]=1001
    return answer

n = int(input())
p = list(map(int, input().split()))
solution(p)