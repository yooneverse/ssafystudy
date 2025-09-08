# 원형 큐 연습 대표 문제: 요세푸스

from collections import deque # 강의를 들어본 결과 덱은 사용불가일 수가 없다는 판단입니다

n, k = map(int, input().split())

q = deque(range(1, n+1)) #원형 큐에 n으로 들어온 수를 하나하나 넣는다는 뜻입니다

result = [] # 제거된 사람들의 명단 같은 역할입니다

while q:
    for _ in range(k-1):
        q.append(q.popleft())   # K-1번 회전
    result.append(q.popleft())  # K번째에 해당하는 데이터 pop으로 제거

print("<", end="") # 이어질 데이터 출력에 있어서 한 줄로 입력하기 위해서는 end=""를 써줍니다 
print(*result, sep=", ", end="") #sep=", "으로 데이터 사이사이에 ,를 끼우고 공백을 넣어줍니다
print(">")
