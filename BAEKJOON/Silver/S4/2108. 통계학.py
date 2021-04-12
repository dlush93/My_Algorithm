import sys
input = sys.stdin.readline


N = int(input())
num_list = [0]*8001
sort_list = []
chk = 0
chk_num = []
for i in range(N):
    num_list[int(input())+4000] += 1

for i in range(8001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            sort_list.append(i-4000)
        if num_list[i] > chk:
            chk = num_list[i]
            chk_num = [i - 4000]
        elif num_list[i] == chk:
            chk_num.append(i - 4000)
print(int(round(sum(sort_list)/N)))
print(sort_list[N//2])
if len(chk_num) >= 2:
    print(chk_num[1])
else:
    print(chk_num[0])
print(sort_list[-1] - sort_list[0])