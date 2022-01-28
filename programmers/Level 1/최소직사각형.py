def solution(sizes):
    row, col = 0, 0
    for size in sizes:
        row = max(row, max(size))
        col = max(col, min(size))
    return row*col

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))