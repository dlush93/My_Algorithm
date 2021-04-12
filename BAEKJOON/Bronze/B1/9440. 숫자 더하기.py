while True:
    data = list(input().split())
    if data == ["0"]:
        break
    else:
        num1=""
        num2=""
        number = sorted(data[1:])
        keep=[]
        for i in number:
            if i =='0':
                keep.append(i)
            else:
                if len(num1) > len(num2):
                    num2 += i
                else:
                    num1 += i
        for k in keep:
            if int(num1) > int(num2):
                num2 = num2[0] + "0" + num2[1:]
            else:
                num1 = num1[0] + "0" + num1[1:]
        print(int(num2)+ int(num1))