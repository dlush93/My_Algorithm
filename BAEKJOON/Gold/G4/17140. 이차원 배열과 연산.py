def find_num(row, col, time):
    global board
    if board[r-1][c-1] == k:
        return time
    if time > 100:
        return -1

    if row >= col:
        row, col, board = row_operation(row, col)
    else:
        row, col, board = col_operation(row, col)

    return find_num(row, col, time+1)


def row_operation(row, col):
    nc = 0
    new_board = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(row):
        nums = dict()
        for j in range(col):
            if board[i][j] == 0:
                continue
            if board[i][j] not in nums:
                nums[board[i][j]] = 0
            nums[board[i][j]] += 1
        nc = max(nc, len(nums)*2)
        temp = sorted(nums.items(), key=lambda x: (x[1], x[0]))
        for n in range(min(50, len(nums))):
            for l in range(2):
                new_board[i][n*2+l] = temp[n][l]
    return row, nc, new_board


def col_operation(row, col):
    nr = 0
    new_board = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(col):
        nums = dict()
        for j in range(row):
            if board[j][i] == 0:
                continue
            if board[j][i] not in nums:
                nums[board[j][i]] = 0
            nums[board[j][i]] += 1
        nr = max(nr, len(nums) * 2)
        temp = sorted(nums.items(), key=lambda x: (x[1], x[0]))
        for n in range(min(50, len(nums))):
            for l in range(2):
                new_board[n*2+l][i] = temp[n][l]
    return nr, col, new_board


r, c, k = map(int, input().split())
board = [[0 for _ in range(100)] for _ in range(100)]
for i in range(3):
    board[i][0], board[i][1], board[i][2] = map(int, input().split())
print(find_num(3, 3, 0))