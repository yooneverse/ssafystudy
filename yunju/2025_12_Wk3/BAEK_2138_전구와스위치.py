'''
N개의 전구와 스위치 (2 <= N <= 100000)
최소 스위치 횟수

불가능한 경우 -1 출력

'''
'''
아이디어

반드시 눌러야 하는 스위치가 있을까?

i번째 전구 입장에서
i-1번째 전구가 목표와 다르다면 
i번째 스위치를 누를 수 밖에 없음
'''
def toggle(arr, idx):
    for i in range(idx-1, idx+2):
        if 0<=i<N:
            arr[i] = 1-arr[i]

def solve(arr,count):
    for i in range(1, N):
        if arr[i-1] != goal[i-1]:
            toggle(arr, i)
            count += 1
    if arr == goal:
        return count
    else:
        return float('inf')

N = int(input())
lights = list(map(int,input()))
goal = list(map(int,input()))

res1 = solve(lights[:],0)
lights[0] = 1-lights[0]
lights[1] = 1-lights[1]
res2 = solve(lights[:], 1)
ans = min(res1, res2)

if ans == float('inf'):
    print(-1)
else:
    print(ans)