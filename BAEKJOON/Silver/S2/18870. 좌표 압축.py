N = int(input())
location = list(map(int, input().split()))
sort_location = sorted(list(set(location)))
dic = {key : value for value, key in enumerate(sort_location)}
result = []
for l in location:
    result.append(dic[l])
print(*result)