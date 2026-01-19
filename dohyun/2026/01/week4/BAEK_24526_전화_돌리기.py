# BAEK 24526. 전화 돌리기
# 위상 정렬, 덱
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 회장이 부원들에게 전화를 넘김
# 부원들도 다른 부원들에게 전화를 넘김
# 같은 부원이 두 번 전화받지 않게 하자.

N, M = map(int, input().split())
call = [[] for _ in range(N + 1)]   # 정방향 배열
reverse_call = [[] for _ in range(N + 1)]   # 역방향 배열
degree = [0] * (N + 1)  # 진출 차수

# 노드간 정방향/역방향 연결, 차수 증가
for _ in range(M):
    u, v = map(int, input().split())
    call[u].append(v)
    reverse_call[v].append(u)
    degree[u] += 1

safe = [False] * (N + 1)    # 전화 걸어도 되면 True
q = deque()
for i in range(1, N + 1):
    # 차수가 0인 부원은 전화 걸어도 됨
    # deque에 추가해서 역방향으로 점검
    if degree[i] == 0:
        q.append(i)
        safe[i] = True

while q:
    x = q.popleft()
    # 역방향으로 진행해서 차수가 0이 되면 전화 걸어도 됨
    for j in reverse_call[x]:
        degree[j] -= 1
        if degree[j] == 0:
            q.append(j)
            safe[j] = True

print(sum(safe))
