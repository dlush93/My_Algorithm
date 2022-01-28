import sys
input = sys.stdin.readline

N = int(input())
length = 0
dot = [list(map(int, input().split())) for i in range(N)]
dot.sort(key=lambda x : (x[1], x[0]))
dot_list = []
temp = []
now_color = dot[0][1]
for i in range(N):
    if dot[i][1] == now_color:
        temp.append(dot[i][0])
    else:
        dot_list.append(temp)
        temp = []
        temp.append(dot[i][0])
        now_color = dot[i][1]
else:
    dot_list.append(temp)

for dots in dot_list:
    for i in range(len(dots)):
        if i == 0:
            length += abs(dots[i+1] - dots[i])
        elif i == len(dots)-1:
            length += abs(dots[i] - dots[i-1])
        else:
            length += min(abs(dots[i+1] - dots[i]),
                          abs(dots[i] - dots[i-1]))
print(length)