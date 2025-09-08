import sys
input = sys.stdin.readline   # 빠른 입력을 위해 sys.stdin.readline 사용

C = int(input())      # 컴퓨터 수
m = int(input())      # 연결된 쌍의 개수

net = [[] for _ in range(C + 1)]   # 인접 리스트 생성
for _ in range(m):
    v, e = map(int, input().split())
    net[v].append(e)   # v와 e 연결
    net[e].append(v)   # e와 v 연결

move = [False] * (C + 1)   # 방문 여부
cnt = 0   # 감염된 컴퓨터 수 (1번 제외)

st = [1]   # 스택에 시작 노드 1 넣기
move[1] = True   # 1번은 방문 처리

while st:
    u = st.pop()   # 현재 컴퓨터 꺼내기
    for nv in net[u]:   # 연결된 컴퓨터 확인
        if not move[nv]:
            move[nv] = True   # 방문 처리
            cnt += 1   # 감염 수 증가
            st.append(nv)   # 스택에 추가

print(cnt)
