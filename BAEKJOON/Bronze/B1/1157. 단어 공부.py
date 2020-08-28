data = input().upper()
alp = set(data)
max_cnt = 0
max_alpha = ''
for i in alp:
    if max_cnt < data.count(i):
        max_cnt = data.count(i)
        max_alpha = i
    elif max_cnt == data.count(i):
        max_alpha = '?'
print(max_alpha)
