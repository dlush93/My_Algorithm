string = ["A"] + list(input())
cnt = 0
for i in range(len(string)-1):
    if abs(ord(string[i]) - ord(string[i+1])) >= 13:
        cnt += 26 - abs(ord(string[i]) - ord(string[i+1]))
    else:
        cnt += abs(ord(string[i]) - ord(string[i+1]))
print(cnt)

