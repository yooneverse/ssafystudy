import sys

input = sys.stdin.readline

# 멀티탭 n구, 전기용품 사용 횟수
n, k = map(int, input().split())

# 전기용품 사용 순서
machine = list(map(int, input().split()))

# 멀티탭 현황
outlet = set()

# 플러그를 뺀 횟수
answer = 0

# 모든 순서를 사용할 때 까지
for i in range(k):
    # 현재 순서 전기용품
    now = machine[i]

    # 멀티탭에 자리가 있으면
    if len(outlet) < n:
        outlet.add(now)

    # 멀티탭에 자리가 없는데, 사용할 전기용품이 꽂혀있지 않을 때
    elif now not in outlet:
        discard = (0, 101)
        # 현재 멀티탭의 전기용품 확인
        for mac in outlet:
            tmp = 1
            # 이후에 사용할 전기용품 확인
            # 가장 늦게 사용하는 전기용품 제거
            for j in range(i + 1, k):
                if machine[j] == mac:
                    if discard[0] < tmp:
                        discard = (tmp, mac)
                    break
                tmp += 1
            # 다시 사용하지 않는 경우 바로 제거
            else:
                discard = (0, mac)
                break
        outlet.remove(discard[1])
        outlet.add(now)
        answer += 1

print(answer)
