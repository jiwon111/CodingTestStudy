def solution(arr):
    answer = []
    answer.append(arr[0])
    cnt=1
    for i in range(1, len(arr)):
        if arr[i]!=answer[i-cnt]:
            answer.append(arr[i])
        else:
            cnt+=1
    return answer
solution([1,1,3,3,0,1,1])