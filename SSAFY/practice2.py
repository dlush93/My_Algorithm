arr = [3,6,7]
n = len(arr)
for i in range(8):
    sub = []
    SUM = 0
    for j in range(n):
        if i & (1<<j):
            sub.append(arr[j])
    for x in range(len(sub)):
        SUM += sub[x]
    if SUM==3:
        print(sub)

# bit =[0,0,0,0]
#
# for i in range(2):
#     bit[0]=i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit)

