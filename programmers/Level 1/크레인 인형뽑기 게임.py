def solution(board, moves):
    answer = 0
    idx = 0
    bucket = [0]
    while idx != len(moves):
        for i in range(len(board)):
            if board[i][moves[idx]-1] != 0:
                if bucket[-1] == board[i][moves[idx]-1]:
                    board[i][moves[idx] - 1] = 0
                    bucket.pop()
                    answer += 2
                else:
                    bucket.append(board[i][moves[idx]-1])
                    board[i][moves[idx]-1] = 0
                break
        idx += 1
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])