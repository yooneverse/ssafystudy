import sys
input = sys.stdin.readline

n, q = map(int, input().split())

sets = [0] * n
for i in range(n):
    size, *ele = map(int, input().split())
    tmp = set(ele)
    sets[i] = tmp

for _ in range(q):
    c, *num = map(int, input().split())

    if c == 1:
        a = num[0] - 1
        b = num[1] - 1
        if len(sets[a]) < len(sets[b]):
            sets[a], sets[b] = sets[b], sets[a]

        sets[a].update(sets[b])
        sets[b].clear()
    else:
        print(len(sets[num[0] - 1]))
