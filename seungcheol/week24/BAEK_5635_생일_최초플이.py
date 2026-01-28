import sys
input = sys.stdin.readline

n = int(input().strip())

old = (0, 1, 1, 2011)
young = (0, 31, 12, 1989)

for _ in range(n):
    name, day, month, year = input().split()
    day = int(day)
    month = int(month)
    year = int(year)

    if old[3] > year:
        old = (name, day, month, year)
    elif old[3] == year and old[2] > month:
        old = (name, day, month, year)
    elif old[3] == year and old[2] == month and old[1] > day:
        old = (name, day, month, year)

    if young[3] < year:
        young = (name, day, month, year)
    elif young[3] == year and young[2] < month:
        young = (name, day, month, year)
    elif young[3] == year and young[2] == month and young[1] < day:
        young = (name, day, month, year)

print(young[0])
print(old[0])
