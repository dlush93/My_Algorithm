N = input()
F = int(input())
front = int(N[0:-2])*100
for i in range(100):
    if front%F == 0:
        print(str(front)[-2:])
        break
    else:
        front += 1
