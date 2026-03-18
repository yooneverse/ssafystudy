from heapq import heappush, heappop
import sys

input = sys.stdin.readline

INF = 2_000_000_005

n, m = map(int, input().split())

edges = [[] for _ in range(n+5)]
edgesR = [[] for _ in range(n+5)]

for i in range(m):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))
    edgesR[v].append((u, w))
    
x, y, z = map(int, input().split())
# y를 안거치는거 먼저 하고 그다음 y거치는거 하면 절약이 될듯함


distx = [INF] * (n + 5)
disty = [INF] * (n + 5)
distyR = [INF] * (n + 5)
distx[x] = 0
disty[y] = 0
distyR[y] = 0

pq = []
heappush(pq, (0, x))

while pq:
    
    cost, cur = heappop(pq)
    
    if distx[cur] != cost:
        continue
    
    for nxt, margin in edges[cur]:
        if nxt == y: continue
        
        if distx[nxt] < cost + margin: continue
    
        heappush(pq, (cost + margin, nxt))
        distx[nxt] = cost + margin


pq = []
heappush(pq, (0, y))
while pq:
    
    cost, cur = heappop(pq)
    
    if disty[cur] != cost:
        continue
    
    for nxt, margin in edges[cur]:
        
        if disty[nxt] < cost + margin:
            continue
        
        heappush(pq, (cost + margin, nxt))
        disty[nxt] = cost + margin


pq = []
heappush(pq, (0, y))
while pq:
    
    cost, cur = heappop(pq)
    
    if distyR[cur] != cost:
        continue
    
    for nxt, margin in edgesR[cur]:
        
        if distyR[nxt] < cost + margin:
            continue
        
        heappush(pq, (cost + margin, nxt))
        distyR[nxt] = cost + margin




# print(disty)
ans1 = distyR[x] + disty[z]
ans2 = distx[z]

if ans1 >= INF:
    ans1 = -1

if ans2 >= INF:
    ans2 = -1

print(ans1, ans2)
# print(distx[z])

        
            
        
        
        
        