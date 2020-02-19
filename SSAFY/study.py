def isp(i):
    token = [[0, '('], [1, '+', '-'], [2, '*', '/']]
    for t in token:
        if i in t:
            return t[0]
def icp(i):
    token = [[3, '('], [1, '+', '-'], [2, '*', '/']]
    for t in token:
        if i in t:
            return t[0]
data = list(input())
stack = []
result = []
for i in data:
    if i.isdecimal():
        result.append(i)
    else:
        if len(stack) ==0:
            stack.append(i)
        elif i == ')':
            while stack.pop() != '(':
                temp = stack.pop()
                result.append(temp)
        else:
            if icp(i) > isp(stack[-1]):
                stack.append(i)
            else:
                result.append(stack.pop())
    print(stack)
    print(result)