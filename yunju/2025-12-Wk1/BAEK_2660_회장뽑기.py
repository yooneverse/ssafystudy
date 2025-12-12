import sys
input = sys.stdin.readline

'''
각 사람마다 다른 사람에게 닿는 최단 거리
플로이드 워셜
'''

N = int(input())
INF = float('inf')
dist = [[INF]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    dist[i][i]=0

score = INF
candidates = []

while True:
    a,b = map(int, input().split())
    if a==-1:
        break
    dist[a][b] = 1
    dist[b][a] = 1

for k in range(1,N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if dist[i][j] > dist[i][k]+dist[k][j]:
                dist[i][j] = dist[i][k]+dist[k][j]

scores = [0]*(N+1)
for i in range(1,N+1):
    max_score = max(dist[i][1:])
    if max_score < score:
        score = max_score
        candidates = [i]
    elif max_score == score:
        candidates.append(i)


candidates.sort()
print(score, len(candidates))
print(*candidates)


