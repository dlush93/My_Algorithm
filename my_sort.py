def my_sort(numbers):
    for j in range(len(numbers)-1):
        for i in range(len(numbers)-j-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    return numbers

print(my_sort([55,7,78,12,42,5,32,651,44]))