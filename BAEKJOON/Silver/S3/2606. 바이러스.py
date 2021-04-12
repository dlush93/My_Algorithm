N = int(input())
net = int(input())
array = [[0]*N for i in range(N)]
chk = [0]*N
for i in range(net):
    i, j = map(int, input().split())
    array[i-1][j-1] = 1
    array[j-1][i-1] = 1
chk_list = []
chk_list.append(array[0])
while len(chk_list) != 0:
    com = chk_list.pop()
    for idx, i in enumerate(com):
        if i == 1 and chk[idx] != 1:
            chk[idx] = 1
            chk_list.append(array[idx])
print(sum(chk)-1)