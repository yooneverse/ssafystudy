# 시간초과

def make_bag(cnt, bag, val):
    global max_val
    # 가지치기, 만약 버틸 수 있는 무게보다 커진다면
    if bag > K:
        return

    # 종료조건. 물건을 다 봤으면
    if cnt == N:
        max_val = max(val, max_val)
        return

    make_bag(cnt+1, bag + weight[cnt], val+value[cnt])
    make_bag(cnt + 1, bag, val)

N, K = map(int, input().split())
weight = []
value = []

# 물건의 무게랑 가치를 다르게 입력받기
for _ in range(N):
    a, b = map(int, input().split())
    weight.append(a)
    value.append(b)

# 원하는 값: 가치의 최댓값
max_val = 0

# 함수 호출
make_bag(0,0,0)
print(max_val)


############### DP ###################


N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (K + 1)  # 무게 0~K까지 최대 가치 저장

# 각 물건을 한 번씩만 사용할 수 있는 0-1 배낭이므로,
# 같은 물건을 중복 사용하지 않도록 '뒤에서 앞으로' 갱신
for w, v in items:
    for k in range(K, w - 1, -1):
        # 현재 물건을 넣었을 때의 가치 후보를 계산 (이전 상태 dp[k - w] + v)
        candidate = dp[k - w] + v

        # 넣지 않았을 때(dp[k])와 넣었을 때(candidate) 중 더 큰 값을 선택
        if candidate > dp[k]:
            dp[k] = candidate
        # else: 그대로 dp[k] 유지

# 배낭 용량이 K일 때의 최대 가치를 출력한다
print(dp[K])
