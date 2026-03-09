# BAEK 2138. 전구와 스위치
import sys
input = sys.stdin.readline

N = int(input())
current = list(map(int, input().strip()))
expect = list(map(int, input().strip()))


def solve(push_first):
    arr = current[:]
    cnt = 0
    if push_first:
        for i in range(2):
            arr[i] ^= 1     # XOR
        cnt = 1
    for i in range(1, N):
        if arr[i - 1] != expect[i - 1]:
            arr[i - 1] ^= 1
            arr[i] ^= 1
            if i + 1 < N:
                arr[i + 1] ^= 1
            cnt += 1
    return cnt if arr == expect else float('inf')


best = min(solve(False), solve(True))
print(best if best != float('inf') else -1)
