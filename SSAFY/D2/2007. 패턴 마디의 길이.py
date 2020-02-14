for t in range(1, int(input())+1):
    words = input()
    for i in range(10):
        if words[0:i+1] == words[i+1:2*(i+1)] == words[2*(i+1):3*(i+1)]:
            print('#{} {}'.format(t, len(words[0:i+1])))
            break