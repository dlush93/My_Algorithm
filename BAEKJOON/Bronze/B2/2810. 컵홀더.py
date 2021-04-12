N = int(input())
seat = list(input())
cnt = 0
for i in seat:
    if i == 'L':
        cnt +=1
cup = (N + 1 - cnt//2)
print(min(N, cup))