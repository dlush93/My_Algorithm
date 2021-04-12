def find_num():
    cnt = 0
    for i in range(1, N+1):
        now = str(i)
        if len(now) <=2:
            cnt += 1
        else:
            dif = int(now[0]) - int(now[1])
            for j in range(1, len(now)-1):
                new_dif = int(now[j]) - int(now[j+1])
                if dif != new_dif:
                    break
            else:
                cnt += 1
    return cnt


N = int(input())
print(find_num())