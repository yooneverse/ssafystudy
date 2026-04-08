'''
제일 처음 위치하는 가로등이 일단 제일 앞까지 비출 수 있는지가 중요함

'''

# 굴다리 길이
N = int(input())
# 가로등 갯수
M = int(input())

# 가로등이 위치하는 곳
lst = list(map(int ,input().split()))

# 하나도 모르겠는데 어캄

def is_possible(h):
        # 1. 시작점(0)을 밝힐 수 있는지 확인
        if lst[0] - h > 0:
            return False
        
        # 2. 가로등 사이의 간격을 밝힐 수 있는지 확인
        for i in range(1, M):
            if lst[i-1] + h < lst[i] - h:
                return False
        
        # 3. 끝점(n)을 밝힐 수 있는지 확인
        if lst[-1] + h < N:
            return False
            
        return True

# 이분 탐색 설정
start = 1
end = N
result = N

while start <= end:
    mid = (start + end) // 2
        
    if is_possible(mid):
        result = mid
        end = mid - 1  # 더 작은 높이가 있는지 확인
    else:
        start = mid + 1 # 높이를 키워야 함

print(result)