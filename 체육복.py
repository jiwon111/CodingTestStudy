def solution(n, lost, reserve):
    answer = 0
    borrow = 0
    real_lost = [i for i in lost if i not in reserve]
    real_reserve = [i for i in reserve if i not in lost]
    real_lost.sort()
    real_reserve.sort()
    #전체-빌릴 수 없는 real_lost 갯수 =리턴값
    for i in range(len(real_lost)):
        if real_lost[i] - 1 in real_reserve:
            borrow += 1
            real_reserve.pop(real_reserve.index(real_lost[i]-1))
        elif real_lost[i]+1 in real_reserve:
            borrow += 1
            real_reserve.pop(real_reserve.index(real_lost[i]+1))
    answer = n - (len(real_lost) - borrow)
    return answer

n = 5
lost = [1, 2, 4]
reserve = [2, 3, 4, 5]#정답 4
solution(n, lost, reserve)
#3, 7, 12, 13, 14 정렬하면-> 3, 5, 7, 12