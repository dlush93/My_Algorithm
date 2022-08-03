N = int(input())
word_dict = dict()
for _ in range(N):
    word = input()
    for idx, w in enumerate(word, 1):
        if w not in word_dict:
            word_dict[w] = 0
        word_dict[w] += 10**(len(word)-idx)
sorted_word = sorted(word_dict, key=lambda x: -word_dict[x])
nums = list(range(9, 9-len(word_dict), -1))
print(sum([word_dict[w]*n for w, n in zip(sorted_word, nums)]))