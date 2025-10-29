# N : 전체 날짜 수 K : 합을 구하기 위한 날짜
N, K = map(int, input().split())
arr = list(map(int ,input().split()))

# 첫번째 구간 합 더해주기
now_sum = sum(arr[:K])
max_sum = now_sum

# 2번째 구간부터 반복
for i in range(K, N):
    # 1) arr[i] 새로 더하고
    # 2) arr[i-K] (이전 구간의 맨 앞값)을 빼줌
    now_sum += arr[i] - arr[i-K]
    
    max_sum = max(max_sum, now_sum)

print(max_sum)