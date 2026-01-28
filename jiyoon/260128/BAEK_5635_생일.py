import sys

# 빠른 입력을 위한 readline 사용(이제는 쓸 때가 됐다 진짜로)
input = sys.stdin.readline

n = int(input())
birthdays = []

for _ in range(n):
    name, day, month, year = input().split()
    
    # 정렬 기준을 맞추기 위해 (년, 월, 일, 이름) 순서로 저장
    birthdays.append((int(year), int(month), int(day), name))

# 생년월일 기준으로 오름차순 정렬
# 가장 먼저 태어난 사람이 앞에, 가장 늦게 태어난 사람이 뒤에 위치함
birthdays.sort()

# 가장 늦게 태어난 사람 출력 (가장 나이가 적음)
print(birthdays[-1][3])

# 가장 먼저 태어난 사람 출력 (가장 나이가 많음)
print(birthdays[0][3])
