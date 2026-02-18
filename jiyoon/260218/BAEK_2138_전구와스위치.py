import sys
input = sys.stdin.readline

def toggle(arr, i):
    n = len(arr)
    for j in (i - 1, i, i + 1):
        if 0 <= j < n:
            arr[j] = '1' if arr[j] == '0' else '0'

def simulate(start, target, press_first):
    arr = start[:]  # 복사
    cnt = 0

    if press_first:
        toggle(arr, 0)
        cnt += 1

    # i-1을 맞추기 위해 i를 결정 (왼쪽부터 확정)
    for i in range(1, len(arr)):
        if arr[i - 1] != target[i - 1]:
            toggle(arr, i)
            cnt += 1

    return cnt if arr == target else float('inf')

n = int(input().strip())
start = list(input().strip())
target = list(input().strip())

ans = min(
    simulate(start, target, False),
    simulate(start, target, True)
)

print(-1 if ans == float('inf') else ans)
