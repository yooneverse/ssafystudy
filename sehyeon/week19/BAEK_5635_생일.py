n = int(input())
std = []

for _ in range(n):
    name, day, month, year = input().split()
    day = int(day)
    month = int(month)
    year = int(year)
    std.append((year, month, day, name))

std.sort()
print(std[-1][3])
print(std[0][3])
