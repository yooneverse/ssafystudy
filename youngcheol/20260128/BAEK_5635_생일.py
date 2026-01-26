# sort 활용법
# n개의 줄에 이름 dd mm yyyy

#첫째 줄에 가장 나이 적은 사람의 이름 둘째줄에 가장 나이 많은 사람의 이름 출력

n = int(input())
student = []

for _ in range(n):
    name, day, month, year = input().split()
    student.append([int(year), int(month), int(day), name])

# sort를 활용해서 순서 정리
student.sort()
print(student[-1][3])

print(student[0][3])