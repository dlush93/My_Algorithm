for t in range(int(input())):
    r, S = input().split()
    R = int(r)
    result = ''
    for i in range(len(S)):
        result += S[i]*R
    print(result)