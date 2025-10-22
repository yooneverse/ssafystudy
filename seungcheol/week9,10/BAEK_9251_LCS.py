first = input()
second = input()

n = len(second)
now = [0] * (n + 1)

for f in first:
    prev = now[:]
    now = [0] * (n + 1)
    for i in range(1, n + 1):
        if f == second[i - 1]:
            now[i] = prev[i - 1] + 1
        else:
            now[i] = max(now[i - 1], prev[i])

print(now[n])
