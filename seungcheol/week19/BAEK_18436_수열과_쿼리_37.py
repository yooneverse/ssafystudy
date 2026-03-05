import sys
input = sys.stdin.readline

n = int(input().strip())

lst = list(map(int, input().split()))

size = 1
while size < n:
    size <<= 1
tree = [0] * (2 * size)

def build(s, e, i=1):
    if s == e:
        if lst[s] % 2:
            tree[i] = (1, 0)
        else:
            tree[i] = (0, 1)
        return tree[i]
    mid = (s + e) // 2
    left = build(s, mid, i*2)
    right = build(mid+1, e, i*2+1)
    tree[i] = (left[0] + right[0], left[1] + right[1])
    return tree[i]

build(0, n-1)

def search(s, e, l, r, odd, i=1):
    if e < l or s > r:
        return 0

    if l <= s and e <= r:
        return tree[i][odd]

    mid = (s + e) // 2
    return search(s, mid, l, r, odd, i*2) + search(mid+1, e, l, r, odd, i*2+1)

def update(s, e, idx, diff, i=1):
    if s > idx or idx > e:
        return

    tree[i] = (tree[i][0] + diff[0], tree[i][1] + diff[1])

    if s != e:
        mid = (s + e) // 2
        update(s, mid, idx, diff, i*2)
        update(mid+1, e, idx, diff, i*2+1)

m = int(input().strip())

for _ in range(m):
    a, b, c = map(int, input().split())

    if a == 1:
        if lst[b - 1] % 2 != c % 2:
            if c % 2:
                update(0, n-1, b-1, (1, -1))
            else:
                update(0, n-1, b-1, (-1, 1))
        lst[b - 1] = c
    elif a == 2:
        print(search(0, n-1, b-1, c-1, 1))
    else:
        print(search(0, n-1, b-1, c-1, 0))

