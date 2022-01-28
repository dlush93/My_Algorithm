data = list(input())
stick = 0
cnt = 0
for i in range(len(data)):
    if data[i] == '(':
        if data[i+1] == ')':
            cnt += stick
        else:
            stick += 1
    elif data[i]== ')' and data[i-1] != '(':
        stick -= 1
        cnt += 1
print(cnt)