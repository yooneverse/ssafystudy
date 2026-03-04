# BAEK 2668. 숫자고르기
import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

numbers = [0]
for i in range(N):
    numbers.append(int(input()))

# index 값을 저장해둬야 하나?
# 아니면 바로 찾으러 가는게 좋을까?
# visited 배열로 방문 체크해보자


# # 부분집합으로 계산하기 실패
# nums = []
# selected = []
result = []


# def dfs(idx):
#     global result
#     if idx > N:
#         if set(nums) == set(selected) and len(result) < len(selected):
#             result = nums[:]
#             return
#         return
#     if numbers[idx] not in selected and not visited[idx]:
#         visited[idx] = True
#         nums.append(idx)
#         selected.append(numbers[idx])
#         dfs(idx+1)
#         nums.pop()
#         selected.pop()
#         visited[idx] = False
#     dfs(idx+1)


# dfs(1)
visited = [False] * (N + 1)
# print(len(result))
# for n in result:
#   print(n)

# 사이클 판단


def dfs(idx, idx_lst):
    global result
    if visited[idx]:
        return
    if idx == start:
        result += idx_lst
        return
    visited[idx] = True
    dfs(numbers[idx], idx_lst + [idx])
    visited[idx] = False


for i in range(1, N+1):
    if i not in result:
        start = i
        dfs(numbers[i], [i])

result.sort()
print(len(result))
for n in result:
    print(n)
