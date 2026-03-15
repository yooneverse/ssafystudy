import sys

input = sys.stdin.readline

'''
세로 N 가로 M 
인벤토리 시작 B개
제거하여 넣기 2초
올리기 1초

최소 시간과 땅의 높이(최대)
'''

N, M, B = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 최소 시간
a_time = float('inf')
a_height = 0

for h in range(257):
    build = 0
    remove = 0
    for r in range(N):
        for c in range(M):
            if graph[r][c] > h:
                remove += graph[r][c] - h
            elif graph[r][c] < h:
                build += h - graph[r][c]

    if remove + B < build:
        continue
    time = remove * 2 + build
    if a_time >= time:
        a_time = time
        a_height = h

print(a_time, a_height)