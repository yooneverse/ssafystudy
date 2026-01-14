def password(idx, w, c, cnt, word):
    if cnt == L:
        if not w:
            return
        if c < 2:
            return
        print(word)
        return

    for i in range(idx, C):
        if alpha[i] in vowel:
            password(i + 1, w + 1, c, cnt + 1, word + alpha[i])
        else:
            password(i + 1, w, c + 1, cnt + 1, word + alpha[i])

L, C = map(int, input().split())

alpha = list(input().split())

alpha.sort()

vowel = ['a', 'e', 'i', 'o', 'u']

password(0, 0, 0, 0, '')
