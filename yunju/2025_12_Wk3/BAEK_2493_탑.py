'''
일직선 위 N개의 높이가 서로 다른 탑
수평 직선의 왼쪽부터 오른쪽 방향으로 세움

각 탑 꼭대기 레이저 송신기 설치

평행하게 수평 직선의 왼쪽 방향으로 발사

기둥 모두에 신호 수신 장치 설치

가장 먼저 만나는 하나의 탑에서만 수신 가능

'''
'''
아이디어

맨 오른쪽 숫자부터 꺼냄
본인보다 큰 숫자 나오면 해당 인덱스

작은 숫자가 위에 오도록
'''
N = int(input())
height = list(map(int, input().split()))

# (idx, height)를 저장
stack = []
result = [0]*N
for i in range(N-1,-1,-1):
    if stack:
        while stack and stack[-1][1] <= height[i]:
            idx, h = stack.pop()
            result[idx] = i+1
    stack.append((i, height[i]))

print(*result)

