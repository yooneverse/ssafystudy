# BAEK 2606. 바이러스
# 덱 사용
from collections import deque

N = int(input())
pair = int(input())
dq = deque()

# 자식 2차원 배열 생성
child = [[] for _ in range(N + 1)]

# 방문 여부 확인 배열 생성
visited = [0] * (N + 1)

# 1번으로 돌아오지 않도록 방문했다고 설정
visited[1] = 1
cnt = 0     # 바이러스에 감염된 PC 카운트

# 간선 정보 입력
# 화살표 없으므로 쌍방 통행 가능
for _ in range(pair):
    s, e = map(int, input().split())
    child[s].append(e)
    child[e].append(s)

# 만약 1번 컴퓨터에서 전염된 자식이 있을 경우
# 모든 자식 번호를 덱에 저장 후 방문 기록, 카운트 1 증가
if child[1]:
    for n in child[1]:
        dq.append(n)
        visited[n] = 1
        cnt += 1

# 전염된 자식 존재하면 반복
while dq:
    # 자식 번호 꺼냄
    c = dq.popleft()
    # 자식의 자손이 있는지 배열로 확인
    if child[c]:
        # 자손에 방문한 적 없으면 덱에 저장 후 방문기록, 카운트 1 증가
        for n in child[c]:
            if visited[n] == 0:
                dq.append(n)
                visited[n] = 1
                cnt += 1

print(cnt)
