col, row = map(int, input().split())
store_num = int(input())
store = [tuple(map(int, input().split())) for _ in range(store_num)]
sdir, sdist = map(int, input().split())

total = 0
for stdir, stdist in store:
    if sdir == stdir:
        total += abs(stdist - sdist)
    elif abs(sdir - stdir) == 1:
        if (sdir + stdir) == 3:
            total += row + min(sdist + stdist, 2 * col - sdist - stdist)
        elif (sdir + stdir) == 7:
            total += col + min(sdist + stdist, 2 * row - sdist - stdist)
        elif (sdir + stdir) == 5:
            total += (sdist + row - stdist) if sdir == 2 else (stdist + row - sdist)
    elif abs(sdir - stdir) == 2:
        if (sdir + stdir) == 4:
            total += sdist + stdist
        elif (sdir + stdir) == 6:
            total += col - sdist + row - stdist
    elif abs(sdir - stdir) == 3:
        if (sdir + stdir) == 5:
            total += (sdist + col - stdist) if sdir == 4 else (stdist + col - sdist)
print(total)