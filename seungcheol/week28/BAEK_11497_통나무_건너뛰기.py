import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    tree = list(map(int, input().split()))
    tree.sort()
    answer = 0
    for i in range(n-2):
        answer = max(answer, abs(tree[i] - tree[i + 2]))

    print(answer)
