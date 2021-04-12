def wind(direction, place):
    global dust
    keep = 0
    y, x = place
    if direction == 1:
        dy, dx = [0, -1, 0, 1], [1, 0, -1, 0]
    else:
        dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

    for i in range(4):
        while 0 <= y <= R-1 and 0 <= x + <= C-1 :



def dust_diffusion():
    pass

R, C, T = map(int, input().split())
dust = [list(map(int, input().split())) for i in range(R)]
# print(R,C,T)
# print(dust)
now = 0
array = [[0]*C for i in range(R)]
air = []
for i in range(R):
    for j in range(C):
        if dust[i][j] == -1:
            air.append([i,j])

wind(1, air[0])