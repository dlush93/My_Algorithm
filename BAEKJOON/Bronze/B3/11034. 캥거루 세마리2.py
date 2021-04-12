while True:
    try:
        kang = list(map(int, input().split()))
        print(max(kang[2]-kang[1]-1, kang[1]-kang[0]-1))
    except:
        break