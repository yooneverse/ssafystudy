N = int(input())

# 대기시간이 짧은 순으로 정렬
lst = sorted(list(map(int, input().split())))

answer = 0

cnt = N

for i in range(N):
    answer += cnt * lst[i]
    cnt -= 1

print(answer)