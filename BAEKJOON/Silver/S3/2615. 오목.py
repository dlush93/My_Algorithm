dy, dx = [1,1,0,-1], [0,1,1,1]
def omok(node):
    stack = list()
    stack.append(node)
    a = data[y][x]
    while len(stack) !=5:
        y, x = stack[-1]
        if data[y][x] ==a:
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if data[ny][nx] == a:
                    stack.append([ny,nx])
        else:
            break

data = [list(map(int, input().split())) for i in range(19)]
for j in range(19):
    for i in range(19):
