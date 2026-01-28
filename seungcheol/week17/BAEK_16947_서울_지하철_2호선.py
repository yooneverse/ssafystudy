import sys
input = sys.stdin.readline

# 최초 풀이
def check(start, prev):
    if len(edges[start]) == 1:
        return False

    for next_station in edges[start]:
        if next_station == prev:
            continue

        if cycle[next_station] == 1:
            continue

        if cycle[next_station] == -1:
            cycle[next_station] = 1
            cycle[start] = 1
            return True

        cycle[next_station] = -1

        if check(next_station, start):
            if cycle[start] == 1:
                return False
            cycle[start] = 1
            return True
    return False

def subway(start, prev, dist):
    answer[start] = dist
    if len(edges[start]) == 1:
        return

    for next_station in edges[start]:
        if next_station == prev:
            continue
        subway(next_station, start, dist + 1)
    return

# 정거장 수
N = int(input().strip())

# 연결된 노선
edges = [[] for _ in range(N + 1)]
for i in range(N):
    s, e = map(int, input().split())
    edges[s].append(e)
    edges[e].append(s)

# 최소 3거리
cross = []

# 정답
answer = [0] * (N + 1)

# 순환선
cycle = [0] * (N + 1)

# 3거리 저장
for i in range(1, N + 1):
    if len(edges[i]) > 2:
        cross.append(i)

# 3거리가 있는 경우
if len(cross):
    # 순환선 확인
    cycle[cross[0]] = -1
    check(cross[0], 0)

    # 거리 확인
    for station in cross:
        if cycle[station] != 1:
            continue
        for next_station in edges[station]:
            if cycle[next_station] == 1:
                continue
            subway(next_station, station, 1)

print(*answer[1:])
