arr = [int(x) for x in input()]

count = [0]*12
for j in range(len(arr)):
    count[arr[j]] +=1
print(count)
i =1
triple = 0
run = 0
while i<len(count):
    if count[i] != 0 and count[i+1] != 0 and count[i+2] !=0 :
        run +=1
        count[i] -= 1
        count[i+1] -=1
        count[i+2] -=1
        continue
    if count[i]>=3:
        run += 1
        count[i] -= 3
        continue
    i +=1
if triple + run ==2:
    print('baby-gin!')
else:
    print('lose')

