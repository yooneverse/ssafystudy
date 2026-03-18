'''
산성 용액 특성값 -> 1 ~ 1,000,000,000
알칼리성 용액 특성값 -> -1 ~ -1,000,000,000

두 용액을 혼합하여 특성값이 0에 가까운 용액을 제작

동일한 종류 두개 합해도 됨

0에 가장 가까운 용액 만들어 내는 프로그램 

-> 투포인터.. 
'''

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))  

min_liquid = float('inf')
result = (lst[0], lst[1])

left = 0
right = N - 1

while left < right:
    liquid = lst[left] + lst[right]

    # 포인터 이동 전에 확인하기
    if abs(liquid) < min_liquid:
        min_liquid = abs(liquid)
        result = (lst[left], lst[right])

    if liquid == 0:
        break
    
    elif liquid < 0:
        left += 1
        
    else:
        right -= 1

print(result[0], result[1])
