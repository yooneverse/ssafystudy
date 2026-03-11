import sys
input = sys.stdin.readline

n = int(input())
start = list(input().strip())   # 초기 전구 상태
target = list(input().strip())  # 목표 전구 상태


# 스위치를 누르면 idx-1, idx, idx+1 전구 상태가 반전됨
def push(bulbs, idx):
    for i in (idx - 1, idx, idx + 1):
        if 0 <= i < n:
            bulbs[i] = '1' if bulbs[i] == '0' else '0'


# 첫 번째 스위치를 눌렀는지 여부에 따라 시뮬레이션
def simulate(first_push):
    bulbs = start[:]   # 원본 보호용 복사
    count = 0

    # 0번 스위치를 누르는 경우
    if first_push:
        push(bulbs, 0)
        count += 1

    # 왼쪽 전구부터 하나씩 맞춰 나감
    for i in range(1, n):
        if bulbs[i - 1] != target[i - 1]:
            push(bulbs, i)
            count += 1

    # 목표 상태와 같으면 횟수 반환, 아니면 불가능
    if bulbs == target:
        return count
    else:
        return float('inf')


# 두 가지 경우 시도
case1 = simulate(False)   # 첫 스위치 안 누름
case2 = simulate(True)    # 첫 스위치 누름

answer = min(case1, case2)

if answer != float('inf'):
    print(answer)
else:
    print(-1)