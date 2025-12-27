import sys
input = sys.stdin.readline
n = int(input())
one, two = map(int, input().split())
rel = int(input())
parent = [i for i in range(n+1)]
for _ in range(rel):
    p,c = map(int, input().split())
    parent[c] = p

p1 = [one]
p2 = [two]

def find(idx, arr):
    if parent[idx] == idx:
        return
    arr.append(parent[idx])
    return find(parent[idx], arr)

find(one, p1)
find(two, p2)
length1 = len(p1)
length2 = len(p2)
if p1[-1] != p2[-1]:
    print(-1)

else:
    idx = -1
    while length1+idx >= 0 and length2+idx >=0 and p1[idx] == p2[idx]:
        idx -= 1

    if p1[0] == p2[idx+1] or p2[0] == p1[idx+1]:
        print(abs(length1-length2))
    else:
        idx += 1
        print(length1+length2+2*idx)