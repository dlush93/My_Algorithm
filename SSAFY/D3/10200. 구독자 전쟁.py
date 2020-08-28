for t in range(1, int(input())+1):
    N, A, B = map(int, input().split())
    min_people = min(A,B)
    max_people = A + B - N
    if max_people <= 0:
        print('#{} {} {}'.format(t, min_people, 0))
    else:
        print('#{} {} {}'.format(t, min_people, max_people))