N = int(input())
room = 1
start = 1
for i in range(1000000000):
    start += 6 * i
    if N == 1:
        print(room)
        break
    elif N > start and N <= start + 6 * (i + 1):
        room = i + 2
        print(room)
        break