def backtracking(k, word_chk):
    if len(result) > 1:
        if ord(result[-1]) < ord(result[-2]):
            return
    if k == L and 2 <= word_chk < L:
        print(''.join(result))
    else:
        for i in range(C):
            if not chk[i]:
                chk[i] = True
                result.append(password[i])
                if password[i] not in ('a', 'e', 'i', 'o', 'u'):
                    word_chk += 1
                    backtracking(k+1, word_chk)
                    result.pop()
                    word_chk -= 1
                    chk[i] = False
                else:
                    backtracking(k + 1, word_chk)
                    result.pop()
                    chk[i] = False


L, C = map(int, input().split())
password = sorted(list(input().split()))
chk = [False for _ in range(C)]
result = []
backtracking(0, 0)