def chk_sudoku(col, row):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(9):
        if sudoku[col][i] in numbers:
            numbers.remove(sudoku[col][i])
        if sudoku[i][row] in numbers:
            numbers.remove(sudoku[i][row])

    col, row = col-col%3, row-row%3
    for i in range(col, col+3):
        for j in range(row, row+3):
            if sudoku[i][j] in numbers:
                numbers.remove(sudoku[i][j])

    return numbers

def backtracking(cnt):
    global flag
    if flag:
        return
    if cnt == len(blank):
        for i in sudoku:
            print(*i)
        flag = True
        return
    else:
        number = chk_sudoku(blank[cnt][0], blank[cnt][1])

        for num in number:
            sudoku[blank[cnt][0]][blank[cnt][1]] = num
            backtracking(cnt+1)
            sudoku[blank[cnt][0]][blank[cnt][1]] = 0


sudoku = [list(map(int, input().split())) for i in range(9)]
blank = [[i, j] for i in range(9) for j in range(9) if sudoku[i][j] == 0]
flag = False
backtracking(0)