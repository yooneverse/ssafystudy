import sys
input = sys.stdin.readline

n = int(input().strip())

lst = list(map(int, input().split()))

from itertools import permutations

perm = list(permutations(lst, n))

answer = 0

for p in perm:
    tmp = 0
    for i in range(n - 1):
        tmp += abs(p[i] - p[i + 1])
    answer = max(answer, tmp)

print(answer)
