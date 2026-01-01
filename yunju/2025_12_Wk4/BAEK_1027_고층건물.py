N = int(input())
buildings = list(map(int, input().split()))

max_visible = 0

for i in range(N):
    count = 0
    max_slope = -float('inf')
    for j in range(i+1, N):
        dx = j - i
        dy = buildings[j] - buildings[i]
        slope = dy / dx
        if slope > max_slope:
            max_slope = slope
            count += 1

    min_slope = float('inf')
    for j in range(i-1, -1, -1):
        dx = j - i
        dy = buildings[j] - buildings[i]
        slope = dy / dx
        if slope < min_slope:
            min_slope = slope
            count += 1

    if count > max_visible:
        max_visible = count

print(max_visible)