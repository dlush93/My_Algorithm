from copy import deepcopy
def max_price(price_list):
    global max_money

    save_list = price_list.copy()
    temp = max_money
    for i in range(len(price_list)-1):
        for j in range(len(price_list), i, -1):
            result = ''
            if price_list[i] <= price_list[j]:
                price_list[i], price_list[j] = price_list[j], price_list[i]
                for k in price_list:
                    result += str(k)
                if int(result) >= temp:
                    temp = int(result)
            price_list = save_list.copy()
    max_money = temp
    return list(map(int, list(str(temp))))

for t in range(1, int(input())+1):
    price, time = map(int, input().split())
    price_list = list(map(int, list(str(price))))
    max_money = price
    for i in range(time):
        price_list = max_price(price_list)
    print('#{} {}'.format(t, max_money))