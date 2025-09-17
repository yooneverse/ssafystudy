from collections import deque


def BFS(q):
    global answer

    # 기저조건: 더이상 연결된 컴퓨터가 없으면 종료
    if not q:
        return

    # 현재 컴퓨터
    tmp = q.popleft()
    # 컴퓨터 수 +1
    answer += 1

    # 현재 컴퓨터에 연결된 컴퓨터 큐에 추가
    for node in computer[tmp]:
        # 감염이 안되어 있는 경우에 추가
        if visited[node]:
            visited[node] = 0
            q.append(node)
    # 재귀
    BFS(q)

# 컴퓨터 수
N = int(input())

# 회선 수
edge = int(input())

# 인덱스 번호의 컴퓨터에 연결된 컴퓨터 리스트
computer = [[] for _ in range(N + 1)]

# 감염 컴퓨터 리스트
visited = [1] * (N + 1)
# 1번 컴퓨터 감염
visited[1] = 0
# 1번 제외한 감염 수를 찾으므로 -1
answer = -1

# 무향성연결
for i in range(edge):
    s, e = map(int, input().split())

    computer[s].append(e)
    computer[e].append(s)

# 1번 숙주부터 시작
que = deque([1])

BFS(que)

print(answer)