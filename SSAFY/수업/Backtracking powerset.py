def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    result = []
    if k == input:
        for i in range(1,k+1):
            print(a[i], end = "")
            print()

    else:
        k +=1
        ncandidates = construct_candidates(c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a,k,input)

def construct_candidates(c):
    c[0] = True
    c[1] = False
    return 2

MAXCANDIDATES = 100
NMAX = 100
a = [0]*NMAX
data=[1,2,3,4,5,6,7,8,9,10]
backtrack(a,0,10)