N = int(input())

lst = list(map(int, input().split()))

# 가장 빠른 방법은 인출을 가장 빠르게 하는 사람 부터 앞에 줄 세우는 것
# 오름차순으로 정렬하자
lst.sort()
# 한 사람이 인출 하는데 드는 시간
one_time = 0
# 모든 사람이 모두 인출 하는데 드는 총 시간
total_time = 0
# 줄 세운대로 인출 시킨다
for i in lst:
    one_time += i
    total_time += one_time

print(total_time)
