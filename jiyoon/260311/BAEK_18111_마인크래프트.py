import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

ground = [list(map(int, input().split())) for _ in range(N)]

best_time = float('inf')
best_height = 0

for target in range(257):  # 0부터 256까지 모든 높이 시도
    remove = 0  # 깎아서 얻는 블록 수
    add = 0     # 쌓는 데 필요한 블록 수

    for i in range(N):
        for j in range(M):
            height = ground[i][j]

            if height > target:
                remove += height - target
            else:
                add += target - height

    # 인벤토리 포함해서 블록이 충분한 경우만 가능
    if B + remove >= add:
        time = remove * 2 + add

        # 시간이 더 적으면 갱신
        # 시간이 같으면 더 높은 높이로 갱신
        if time < best_time or (time == best_time and target > best_height):
            best_time = time
            best_height = target

print(best_time, best_height)