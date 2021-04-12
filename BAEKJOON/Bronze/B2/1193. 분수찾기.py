x = int(input())
start_num = 1
plus_num = 1
while True:
    if start_num <= x < start_num + plus_num:
        break
    else:
        start_num += plus_num
        plus_num += 1
if plus_num%2:
    a = plus_num - (x - start_num)
    b = x - start_num + 1
else:
    a = x - start_num + 1
    b = plus_num - (x - start_num)
print('{}/{}'.format(a,b))