# BAEK 2467. 용액
import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split()))

# 왼쪽과 오른쪽 더해보면서 최솟값 찾기
# 비교 시에는 절댓값 사용
min_sum = float('inf')
left, right = 0, N - 1

while True:
    # 양 쪽 idx가 같으면 저장된 특성값 출력
    if left == right:
        print(liquid[co_l], liquid[co_r])
        break
    
    # 특성값의 합이 0이면 특성값 출력
    if liquid[left] + liquid[right] == 0:
        print(liquid[left], liquid[right])
        break
    # 특성값의 합이 양수이면 오른쪽 idx 줄임
    elif liquid[left] + liquid[right] > 0:
        if min_sum > liquid[left] + liquid[right]:
            min_sum = liquid[left] + liquid[right]
            co_l, co_r = left, right
        right -= 1
    # 특성값의 합이 음수이면 왼쪽 idx 늘림
    else:
        if min_sum > abs(liquid[left] + liquid[right]):
            min_sum = abs(liquid[left] + liquid[right])
            co_l, co_r = left, right
        left += 1

