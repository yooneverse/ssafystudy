
# N: 스크린 칸 수, M: 바구니 칸 수
n, m = map(int, input().split())
j = int(input())

# 바구니의 현재 왼쪽 끝과 오른쪽 끝 위치
left = 1
right = m
distance = 0

#제미나이 도움받음...
for _ in range(j):
    apple = int(input())
    
    # 1. 사과가 바구니 오른쪽에 떨어지는 경우
    if apple > right:
        move = apple - right
        distance += move
        right = apple
        left += move
        
    # 2. 사과가 바구니 왼쪽에 떨어지는 경우
    elif apple < left:
        move = left - apple
        distance += move
        left = apple
        right -= move
    
    # 3. 사과가 바구니 범위 내에 떨어지는 경우 (이동 거리 0)
    else:
        continue

print(distance)