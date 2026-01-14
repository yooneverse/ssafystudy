# 첫 줄에는 멀티탭 구멍의 개수 N (1 ≤ N ≤ 100)과 전기 용품의 총 사용횟수 K (1 ≤ K ≤ 100)가 정수로 주어진다. 두 번째 줄에는 전기용품의 이름이 K 이하의 자연수로 사용 순서대로 주어진다. 
# 각 줄의 모든 정수 사이는 공백문자로 구분되어 있다.
# 하나씩 플러그를 빼는 최소의 횟수를 출력하시오.

import sys
input = sys.stdin.readline

# N: 멀티탭 구멍 수
# K: 전기용품 사용 횟수
N, K = map(int, input().split())
seq = list(map(int, input().split()))

plug = []   # 현재 멀티탭에 꽂힌 기기들   
ans = 0

# 사용 순서를 하나씩 확인함
for i in range(K):
    now = seq[i]

    # 이미 꽂혀 있으면 패스함
    if now in plug:
        continue

    # 빈 자리 있으면 그냥 꽂음
    if len(plug) < N:
        plug.append(now)
        continue

    # 멀티탭이 꽉 찬 경우 -> 하나를 뽑아야 함
    remove_target = None      # 뽑을 전기용품
    latest_use = -1           # 가장 늦은 다음 사용 시점

    for p in plug:
        # 앞으로 다시 사용되지 않는 전기용품이면 바로 뽑아라
        if p not in seq[i+1:]:
            remove_tar = p
            break
        else:
            # 앞으로 언제 다시 사용되는지 확인함
            next_idx = seq[i+1:].index(p)

            # 더 나중에 쓰이는 전기용품이면 갱신함
            if next_idx > latest_use:
                latest_use = next_idx
                remove_tar = p

    plug.remove(remove_tar)
    plug.append(now)
    ans += 1

print(ans)
