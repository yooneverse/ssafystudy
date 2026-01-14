import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temp = list(map(int, input().split()))

sum_temp = 0

for i in range(K):
    sum_temp += temp[i]
answer = sum_temp

for j in range(N - K):
    sum_temp -= temp[j]
    sum_temp += temp[j + K]
    answer = max(sum_temp, answer)

print(answer)
