'''
전화 넘기기

회장이 한 사람에게 전화를 걸며 시작
전화를 받은 부원은 다른 사람에게 전화를 검
한 사람이 두 번 이삳 전화를 받아서는 안 됨

어떤 부원이 전화를 받았을 때 다른 부원에게 전화를 넘기는 관계를 줌
회장이 전화를 넘길 수 있는 사람의 수 출력
'''

'''
예시
6 6
1 2
2 3
3 4
3 5
3 6
5 2

부장이 1한테 전화 거는 경우 
1은 2에게, 2는 3에게, 3은 5에게, 5는 2에게 전화를 걸게 되면서 
2가 두 번 전화를 받게 됨 
실패!

부장이 4에게 전화거는 경우
4는 누구에게도 전화 걸지 않음
성공!

싸이클이 안 생기게 하는 문제임
왜 소재를 전화로 해서 헷갈리게 하는지
바톤을 전달한다고 생각
'''
'''
특이점

모든 부원이 전화를 받아야 하는(MST) 게 아니라 
그저 한 부원이 여러 번 전화를 받지 않기만 하면 됨

'''
'''
2 <= N <= 100000
1 <= M <= 500000
숫자가 좀 큼

그냥 input 쓰면 시간 초과
input = sys.stdin.readline 하면 통과
input은 한 줄마다 줄바꿈 문자를 검사. 비용이 큼
sys.stdin.readline은 그냥 한 줄 그대로 읽어옴 

대량 데이터 처리 시 주의
'''
import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int, input().split())

# i번 사람이 전화를 거는 사람이 아닌,
# i번 사람에게 전화를 거는 사람을 저장
rev_connect = [[] for _ in range(N+1)]

# i번 사람이 전화를 해야 하는 횟수를 저장
# 한 번 전화를 걸 때마다 1씩 감소시킬 것임
# 값이 0이 된다면 >> 더 이상 전화 걸지 못함 >> 싸이클이 끊김 : 이 사람한테 전화해도 됨
out_degree = [0] * (N+1)

for _ in range(M):
    s, e = map(int, input().split())
    rev_connect[e].append(s) # 역방향 저장. e에게 전화할 수 있는 사람들
    out_degree[s] += 1 # s가 전화해야 하는 횟수 증가

# 아무에게도 전화하지 않는 사람
q = deque()

# 아무에게도 전화하지 않는 사람
for i in range(1, N+1):
    if out_degree[i] == 0:
        q.append(i)

ans = 0

# 전화할 사람이 없어지면 그 사람한테 전화해도 됨
while q:
    nxt = q.popleft()
    ans += 1

    # nxt는 누구에게 전화를 받았는가
    # nxt에게 전화를 걸 수 있는 사람
    # 전화 횟수 1 줄임
    for prev in rev_connect[nxt]:
        out_degree[prev] -= 1

        # nxt에게 전화를 건 사람이 더 이상 전화할 사람이 없다면 q에 추가
        if out_degree[prev] == 0:
            q.append(prev)
print(ans)
