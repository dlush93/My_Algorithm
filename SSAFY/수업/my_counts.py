arr = [int(x) for i in input()]
1 1 2 2 3 3 1 2 5
# def my_counts(numbers):
#     result = []
#     for

def counting_sort(a,b,k):
    c = [0]*k
    for i in range(0. len(b)):
        c[a[i]] += 1
    for i in range(1,len(c)):
        c[i] += c[i-1]
    for i in range(len(b)-1, -1, -1):
        b[c[a[i]]-1] = a[i]
        c[a[i]] -= 1
