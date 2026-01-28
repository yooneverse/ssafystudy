import sys
input = sys.stdin.readline

n = int(input().strip())
dice = list(map(int, input().split()))

second = third = 151

for i in range(6):
    for j in range(i + 1, 6):
        if i + j == 5:
            continue
        second = min(second, dice[i] + dice[j])
        for k in range(j + 1, 6):
            if i + k == 5 or j + k == 5:
                continue
            third = min(third, dice[i] + dice[j] + dice[k])

answer = 0

if n == 1:
    dice.sort()
    answer += dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
else:
    # 2면
    line = (2 * n - 3) * 4
    answer += line * second

    # 1면
    one = 5 * (n ** 2) - line * 2 - 12
    answer += one * min(dice)

    # 3면
    answer += 4 * third

print(answer)
