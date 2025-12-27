'''
앞마당 길이 N
위치 1부터 위치 N까지 눈 쌓임
위치 i에 눈이 ai만큼 쌓임

M초 동안 눈덩이를 굴려 눈사람 만들기
눈덩이 위치 0에서 크기 1으로 시작

두 가지 방법
1. +1 칸으로 굴리기

2. +2 칸으로 던지기
- 기존의 절반된 후 더해짐

0이 되기도 함

대회 시간 내 눈덩이 최대 크기

'''

'''
dp로 풀 수 있을 거 같은데
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
road = list(map(int, input().split()))
ans = 1

def solve(loc, size, time):
    global ans

    if time == M:
        ans = max(ans, size)
        return

    if loc == N-1:
        ans = max(ans,size)
        return

    if loc+1 < N:
        solve(loc+1, size+road[loc+1], time+1)

    if loc+2 < N:
        solve(loc+2, (size//2) + road[loc+2], time+1)


solve(-1,1,0)
print(ans)