def isp(i):
    token = [[0, '('], [1, '+'], [2, '*']]
    for t in token:
        if i in t:
            return t[0]


def icp(i):
    token = [[3, '('], [1, '+'], [2, '*']]
    for t in token:
        if i in t:
            return t[0]

def operator(j, a, b):
    if j == '+':
        return str(int(a) + int(b))
    else:
        return str(int(a)*int(b))

for t in range(1, 11):
    N = int(input())
    data = input()
    stack = []
    result = []
    for i in data:
        if i.isdecimal():
            result.append(i)
        else:
            if i == ')':
                while stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()
            else:
                if len(stack) == 0:
                    stack.append(i)
                elif icp(i) > isp(stack[-1]):
                    stack.append(i)
                else:
                    result.append(stack.pop())
                    stack.append(i)
    for i in range(len(stack)):
        result.append(stack.pop())

    for j in result:
        if j.isdecimal():
            stack.append(j)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(operator(j, a, b))
    print('#{} {}'.format(t, stack[-1]))