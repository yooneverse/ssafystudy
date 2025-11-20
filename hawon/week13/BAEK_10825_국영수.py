N = int(input())
students = []

for _ in range(N):
    name, k, e, m = input().split()
    students.append((name, int(k), int(e), int(m)))

# 정렬: (-국어, 영어, -수학, 이름)
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for s in students:
    print(s[0])
