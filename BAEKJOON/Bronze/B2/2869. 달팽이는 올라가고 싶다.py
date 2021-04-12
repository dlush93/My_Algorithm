A, B, V = map(int, input().split())
height = 0
day = 0
if (V-A)%(A-B) == 0:
    day = (V-A)//(A-B) + 1
else:
    day = (V-A)//(A-B) + 2
print(day)