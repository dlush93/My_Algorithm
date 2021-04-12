cnt = 0
for t in range(int(input())):
    word = input()
    chk = []
    group = word[0]
    for i in range(len(word)):
        now = word[i]
        if now == group:
            continue
        elif now != group and now not in chk:
            chk.append(group)
            group = now
        else:
            break
    else:
        cnt += 1
print(cnt)