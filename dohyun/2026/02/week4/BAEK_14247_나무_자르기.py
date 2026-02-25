# BAEK 14247. 나무 자르기
import sys
input = sys.stdin.readline

n = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))

result = 0

# 나무의 초기 상태는 영원히 변하지 않음
# 그럼 나무가 자라는 순서가 중요
# 나무가 조금씩 자라는데 여러 번 써는 것은 개손해
# 그럼 자라는 순으로 정렬해서 마지막에 많이 자라는 나무를 썰자
trees = sorted(zip(A, H))

for i in range(n):
    a, h = trees[i]
    result += h + a * i

print(result)