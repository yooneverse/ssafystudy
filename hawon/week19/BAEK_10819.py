import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))

used = [0] * n

best = 0

def abs_val(x):
    if x < 0:
        return -x
    return x

def dfs(depth, prev_value, current_sum):
    global best

    if depth == n:
        if current_sum > best:
            best = current_sum
        return

    for i in range(n):
        # 아직 안 쓴 원소만 선택
        if used[i] == 0:
            used[i] = 1
            
            # 첫 원소면 차이를 더할 게 없음
            if depth == 0:
                dfs(depth + 1, arr[i], current_sum)
            else:
                # 새로 생기는 점수
                added = abs_val(prev_value - arr[i])
                dfs(depth + 1, arr[i], current_sum + added)

            # 원상복구
            used[i] = 0

dfs(0, 0, 0)
print(best)
