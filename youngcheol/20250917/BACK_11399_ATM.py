N = int(input())
arr = list(map(int, input().split()))

arr.sort()

total = 0  # 각 사람의 소요시간 합

min_time = 0 # 지금까지의 누적 대기 포함시간

for x in arr:
    total += x  # 현재 사람까지 걸리는 시간
    min_time += total  # 이를 전체 합에 더함

print(min_time)

print(arr)



''' 원래 풀었던 방식 
N = int(input())


def digit(idx, selected, now_time):
    global min_time

    # 가지치기
    if now_time >= min_time:
        return

        # 종료조건
    if idx == N:
        min_time = min(now_time, min_time)
        return

    # 재귀 호출
    total = 0
    for i in range(N):
        if not i in selected:
            selected.append(i)
            new_time = now_time + arr[i] + total
            total = new_time
            digit(idx+1, selected, total)
            selected.pop()

arr = list(map(int, input().split()))

min_time = 10 ** 18
digit(0,[],0)

print(min_time)

'''