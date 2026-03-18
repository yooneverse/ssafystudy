import sys
import bisect

'''
bisect 라이브러리
- 정렬된 리스트에서 값을 삽입할 위치를 이진 탐색으로 찾아주는 모듈
- bisect_left(list, x) : x가 들어갈 가장 왼쪽 위치 반환
'''

input = sys.stdin.readline

n = int(input())
book = list(map(int, input().split()))

lis = []

for num in book:
    # num이 들어갈 위치를 이진 탐색으로 찾음
    idx = bisect.bisect_left(lis, num)
    
    # lis 끝에 붙는 경우
    if idx == len(lis):
        lis.append(num)
    else:
        # 해당 위치 값을 더 작은 값으로 갱신
        lis[idx] = num

# 최소 이동 횟수 = 전체 책 - LIS 길이
print(n - len(lis))