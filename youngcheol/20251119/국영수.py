N = int(input().strip())
students = []

for _ in range(N):
    name, k, e, m = input().split()
    k, e, m = int(k), int(e), int(m)
    students.append((name, k, e, m))

    # 4순위: 이름 (오름차순)
    students.sort(key=lambda x: x[0])

    # 3순위: 수학 (내림차순 -> reverse=True)
    students.sort(key=lambda x: x[3], reverse=True)

    # 2순위: 영어 (오름차순)
    students.sort(key=lambda x: x[2])

    # 1순위: 국어 (내림차순)
    students.sort(key=lambda x: x[1], reverse=True)


# 정렬 기준:
# 1) 국어: 내림차순 → -k
# 2) 영어: 오름차순 → e
# 3) 수학: 내림차순 → -m
# 4) 이름: 사전순 오름차순 → name
# students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for s in students:
    print(s[0])
