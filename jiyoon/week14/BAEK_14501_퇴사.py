N = int(input())

for _ in range(N):
    t, p = map(int, input().split())

    # 상담을 할지 말지를 선택하는 재귀적 접근 방법
    def max_get(day, total_get):
    # 현재 날짜와 수익을 넘겨받고 재귀적으로 탐색한다.
    # 상담을 하지 않는 경우와 상담을 하는 경우를 비교하여 최대 수익을 구한다.
        if day >= N:
            return total_get
    # 현재 날짜에 상담을 하지 않고 넘어가는 경우:
    # 1. 다음 날로 넘어가서 다시 재귀적으로 탐색한다.
        no_get = max_get(day+1, total_get)
    # 현재 날짜에 상담을 하는 경우:
    # 1. 상담이 끝난 날을 기준으로 더 이상 상담을 할 수 없다면 그 뒤로 넘어간다.
    # 2. 상담 후 얻을 수 있는 수익과 나머지 날짜에 대한 최대 수익을 더해서 결과를 계산한다.
        yes_get= 0
        if day + t[day] <= N:
            yes_get = max_get(day + t[day], total_get+p[day])
    # 각 경우에서 얻을 수 있는 최대 수익을 비교하여 더 큰 값을 선택한다.
        return max(no_get, yes_get)
    # 최종적으로 첫 번째 날부터 시작하는 최대 수익을 출력한다.
    print(max_get(0, 0))

N = int(input())  # 상담 일수

# 상담 시간과 수익을 리스트로 저장
t = []
p = []

# 상담 시간과 수익 입력 받기
for _ in range(N):
    t_value, p_value = map(int, input().split())
    t.append(t_value)
    p.append(p_value)


# 최대 수익을 계산하는 재귀 함수
def max_get(day, total_get):
    # 종료 조건: 마지막 날을 넘어가면 수익을 반환
    if day >= N:
        return total_get

    # 상담을 하지 않는 경우 (다음 날로 넘어감)
    no_get = max_get(day + 1, total_get)

    # 상담을 하는 경우 (상담을 할 수 있는지 확인)
    yes_get = 0
    if day + t[day] <= N:
        yes_get = max_get(day + t[day], total_get + p[day])

    # 두 경우에서 얻을 수 있는 최대 수익을 반환
    return max(no_get, yes_get)


# 첫 번째 날부터 시작하여 최대 수익을 계산
print(max_get(0, 0))


# ================
# 어떻게든 재귀로 풀어놓고 추천 방법을 찾아봄
# ===============

N = int(input())
T = [0] * (N + 1)
P = [0] * (N + 1)

for i in range(1, N + 1):
    t, p = map(int, input().split())
    T[i] = t
    P[i] = p

# dp[i] = i일부터 마지막 날까지 얻을 수 있는 최대 수익
dp = [0] * (N + 2)

# 뒤에서부터 계산
for day in range(N, 0, -1):
    # 오늘 상담을 했을 때 끝나는 날짜
    end_day = day + T[day]

    # 상담이 퇴사일을 넘기면 못 한다
    if end_day <= N + 1:
        take = P[day] + dp[end_day]
    else:
        take = 0

    # 상담을 안 하면 그냥 다음 날로
    skip = dp[day + 1]

    # 둘 중 최대 선택
    dp[day] = max(take, skip)

print(dp[1])
