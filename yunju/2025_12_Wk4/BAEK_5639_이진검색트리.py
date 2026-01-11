'''
이진검색트리
전위 순회 결과를 받아
후위순회 결과를 출력
'''

'''
전위 순회
중 왼 오

후위 순회
왼 오 중

이진 검색 트리
작은 수는 왼쪽 자식, 큰 수는 오른쪽 자식
'''

'''
입력이 특이
정해져 있지 않음
try, except 사용
'''
import sys
sys.setrecursionlimit(10**6)

nums = []
while True:
    try:
        line = sys.stdin.readline()
        if not line:
            break
        nums.append(int(line))
    except:
        break

# 후위 순회 좌 우 중
# 루트를 기준
def post_order(start, end):
    if start > end:
        return
    root = nums[start]

    idx = end+1

    # 분기점 찾기
    # idx부터 오른쪽 자식임
    for i in range(start+1, end+1):
        if nums[i] > root:
            idx = i
            break

    post_order(start+1, idx-1)
    post_order(idx, end)
    print(root)

post_order(0, len(nums)-1)