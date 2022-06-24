def solution(board, moves):
    answer = 0
    dolls = []
    for i in range(len(moves)):
        for j in range(len(board[moves[i]-1])):
            if board[j][moves[i]-1] != 0:
                dolls.append(board[j][moves[i]-1])
                board[j][moves[i]-1] = 0

                if len(dolls)>1:
                    if dolls[-1] == dolls[-2]:
                        print(dolls)
                        print('-------')
                        dolls.remove(dolls[-1])
                        dolls.remove(dolls[-1])
                        print(dolls)
                        answer+=2
                break
    return answer

board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
moves=[1,5,3,5,1,2,1,4]
solution(board, moves)