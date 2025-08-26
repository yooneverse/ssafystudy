def sum_of_row(arr):
    sums = []
    for row in arr:
        sums.append(sum(row))
    return sums

def sum_of_col(arr):
    sums = []
    trans = list(zip(*arr))
    for col in trans:
        sums.append(sum(col))
    return sums

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    stage = [list(map(int, input().split())) for _ in range(n)]

    rows = sum_of_row(stage)
    cols = sum_of_col(stage)

    max_score = 0
    for i in range(n):
        for j in range(n):
            score = rows[i] + cols[j] - stage[i][j]
            max_score = max(max_score, score)

    print(f'#{test_case} {max_score}')