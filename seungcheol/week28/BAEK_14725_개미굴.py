import sys
input = sys.stdin.readline

n = int(input().strip())

foods = {0: set()}

for _ in range(n):
    t, *tmp = input().split()
    k = int(t)

    key = ""
    for i in range(k):
        if not i:
            key = tmp[i]
            foods[i].add(key)
        else:
            if foods.get((i, key)) is None:
                foods[(i, key)] = {tmp[i]}
            else:
                foods[(i, key)].add(tmp[i])
            key += tmp[i]

def dfs(value, depth):
    if foods.get((depth, value)) is not None:
        lst = list(foods[(depth, value)])
        lst.sort()

        for nxt in lst:
            print("--"*depth, end="")
            print(nxt)
            dfs(value + nxt, depth + 1)

root = list(foods[0])
root.sort()

for r in root:
    print(r)
    dfs(r, 1)
