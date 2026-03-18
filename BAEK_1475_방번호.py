n = input().strip()

count = [0] * 10

for ch in n:
    count[int(ch)] += 1

count[6] = (count[6] + count[9] + 1) // 2
count[9] = 0

print(max(count))