S = input()
z_list = []
o_list = []
temp = ""
for s in S:
    if len(temp) == 0:
        temp += s
    else:
        if temp[-1] == s:
            temp += s
        else:
            if s == "0":
                o_list.append(temp)
                temp = ""
                temp += s
            else:
                z_list.append(temp)
                temp = ""
                temp += s
if temp[-1] == "0":
    z_list.append(temp)
elif temp[-1] == "1":
    o_list.append(temp)
print(min(len(z_list), len(o_list)))