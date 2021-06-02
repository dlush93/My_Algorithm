def bfs():
    

family = int(input())
man1, man2 = map(int, input().split())
group = [[]*(family+1) for i in range(family + 1)]
for i in range(int(input())):
    x, y = map(int, input().split())
    group[x].append(y)
print(group)