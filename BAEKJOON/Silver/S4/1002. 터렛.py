for t in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r = min(r1, r2)
    R = max(r1, r2)
    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
    if distance == 0 and r == R:
        print(-1)
    elif distance == r + R or R == distance + r:
        print(1)
    elif distance > r + R or R > distance + r:
        print(0)
    else:
        print(2)