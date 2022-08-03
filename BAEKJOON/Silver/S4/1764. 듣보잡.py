import sys
input = sys.stdin.readline


N, M = map(int, input().split())
hear = {input().rstrip():'' for _ in range(N)}
name = []
for _ in range(M):
    see = input().rstrip()
    if see in hear:
        name.append(see)
print(len(name))
name.sort()
for n in name:
    print(n)