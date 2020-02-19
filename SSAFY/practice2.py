a = [1,2,3,4,5,6,7,8,9,10]
result = [False] * len(a)
num = 0
def powerset(cnt):
    global num
    if cnt == len(a):

        arr = []
        for i in range(len(result)):
            if result[i] == True:
                arr.append(a[i])
        num+=1
        if sum(arr) == 10 :
            print(arr)

        return
    result[cnt] = True
    powerset(cnt+1)
    print(result)
    result[cnt] = False
    powerset(cnt+1)
    print(result)

powerset(0)
print(num)