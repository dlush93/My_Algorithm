ascending = [1,2,3,4,5,6,7,8]
descending = ascending[::-1]
data = list(map(int, input().split()))
if data == ascending:
    print('ascending')
elif data == descending:
    print('descending')
else:
    print('mixed')