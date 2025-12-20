import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 0: 빈 칸, 1: 집, 2: 치킨집
# r, c는 1부터 시작
# 치킨 거리: 집과 가장 가까운 치킨집 사이의 거리
# 1) 모든 치킨집의 위치 구하기
# 2) M개의 치킨집 조합 구하기
# 3) 치킨집과 집의 거리 구하고 chicken_dist 에 저장
# 4) 조합마다 도시의 치킨 거리 구하기
# 5) 조합별 도시의 치킨 거리 비교해서 최솟값 탐색


def cal(comb_lst):
    sum_dist = 0
    chicken_dists = [[[] for _ in range(N)] for _ in range(N)]
    for k in range(M):
        y, x = stores[comb_lst[k]]
        for i in range(N):
            for j in range(N):
                # 3)
                if grid[i][j] == 1:
                    chicken_dists[i][j].append((abs(y - i) + abs(x - j)))

    for i in range(N):
        for j in range(N):
            # 4)
            if chicken_dists[i][j]:
                sum_dist += min(chicken_dists[i][j])
    return sum_dist


def make_comb(start, comb_lst):
    global res

    if len(comb_lst) == M:
        res = min(res, cal(comb_lst))

    L = len(stores)
    for i in range(start, L):
        comb_lst.append(i)
        make_comb(i + 1, comb_lst)
        comb_lst.pop()


res = float('inf')
# 1)
stores = []
for r in range(N):
    for c in range(N):
        if grid[r][c] == 2:
            stores.append((r, c))

# 2)
make_comb(0, [])
print(res)
