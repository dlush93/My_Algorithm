# n = input()
# if int(n)<10:
#     n = '0'+n
# a = n
# count =1
# while True:
#     n = n[-1] + str(int(n[0]) + int(n[-1]))[-1]
#     if a == n :
#         break
#     count +=1
# print(count)

# n = int(input())
# a = n//10
# b = n%10
# c = (a+b)%10
# d = b*10 + c
# cnt = 1
# while d != n:
#     a = d//10
#     b = d%10
#     c = (a+b)%10
#     d = b*10 +c
#     cnt +=1
# print(cnt)

n = int(input())
d = n
cnt = 0
Flag = True
while Flag or d != n:
    Flag = False
    a = d//10
    b = d%10
    c = (a+b)%10
    d = b*10 +c
    cnt +=1
print(cnt)