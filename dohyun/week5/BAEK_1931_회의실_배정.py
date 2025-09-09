# BAEK 1931. 회의실 배정
N = int(input())
# 입력값의 개수만큼 종료/시작 시간을 저장할 배열 생성
time = [[0] for _ in range(N)]
# 입력값으로 종료/시작 시간 저장
for t in range(N):
    s, e = map(int, input().split())
    time[t] = (e, s)
# 종료되는 시간을 기준으로 오름차순 정렬
# 가장 먼저 끝나는 회의가 첫 번째로 나타남
time.sort()
# 회의 횟수/끝나는 시간 저장할 변수 설정
cnt = end = 0

# 종료/시작 시간 배열으로 반복
for e, s in time:
    # 만약 시작 시간이 종료 시간 뒤라면 회의 횟수 1 증가
    if s >= end:
        cnt += 1
        # 이 회의가 끝나는 시간을 저장하며 다시 반복
        end = e

print(cnt)
