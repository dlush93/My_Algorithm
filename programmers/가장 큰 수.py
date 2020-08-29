#
#
# def solution(numbers):
#     slot = [[] for i in range(10)]
#     for i in numbers:
#         slot[int(str(i)[0])].append(i)
#
#     answer = ''
#     return answer
#
# print(solution([6,10,2]))
numbers = [3, 30, 34, 5, 9]
result = ''
slot = [[] for i in range(10)]
for i in numbers:
    slot[int(str(i)[0])].append(i)
for num in range(10, 0, -1):
    if len(slot[num]) == 1:
        result += str(n)
        continue
    elif len(slot[num]) == 0:
        continue
    else:
        for n in slot[num]:


