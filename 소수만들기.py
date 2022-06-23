from itertools import combinations
def isPrime(n):
    for i in range(2, n):
        if n%i==0:
            return 0
    return 1
  
def solution(nums):
    answer = 0
    combi = list(combinations(nums, 3))
    print(combi)
    for i in range(len(combi)):
        if isPrime(sum(combi[i])):
            print(combi[i])
            answer += 1
    print(answer)
    return answer

nums=	[1, 2, 3, 4]
solution(nums)