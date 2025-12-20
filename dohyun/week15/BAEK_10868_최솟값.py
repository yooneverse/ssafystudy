# BAEK 10868. 최솟값
import sys, math
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
# out = []
for _ in range(N):
    arr.append(int(input()))

# for _ in range(M):
#     a, b = map(int, input().split())
#     # print(min(arr[a:b+1]))
#     out.append(str(min(arr[a:b+1])))
#
# sys.stdout.write('\n'.join(out))


K = math.floor(math.log2(N))

st = [[0] * (K + 1) for _ in range(N)]
log2 = [0] * (N + 1)
for i in range(2, N + 1):
    log2[i] = log2[i // 2] + 1

for i in range(N):
    st[i][0] = arr[i]

for k in range(1, K + 1):
    for i in range(0, N - 2 ** k + 1):
        st[i][k] = min(st[i][k - 1], st[i + 2 ** (k - 1)][k - 1])

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    length = b - a + 1
    k = log2[length]
    print(min(st[a][k], st[b - 2 ** k + 1][k]))
