cocktail = list(map(int, input().split()))
taste = [i%2 for i in cocktail]
mix = 1
if sum(taste) == 0 or sum(taste) == 3:
    for i in range(3):
        mix *= cocktail[i]
elif sum(taste):
    for i in range(3):
        if taste[i] == 1:
            mix *= cocktail[i]
print(mix)