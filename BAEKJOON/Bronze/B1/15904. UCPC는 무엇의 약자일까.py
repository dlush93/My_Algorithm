short = "UCPC"
string = list(input())
keep = []
cnt = 0
result = ""
for i in string:
    if i.isupper():
        keep.append(i)
for k in keep:
    if k == short[cnt]:
        cnt += 1
        result += k
    if result == short:
        print("I love UCPC")
        break
else:
    print("I hate UCPC")