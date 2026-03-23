n = int(input())
trees = list(map(int, input().split()))

trees.sort(reverse=True)

answer = 0

for i in range(n):
    answer = max(answer, trees[i] + i + 1)

print(answer + 1)
