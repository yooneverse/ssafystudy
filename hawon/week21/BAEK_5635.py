import sys
input = sys.stdin.readline

N = int(input())
students = [input().split() for _ in range(N)]


old = students[0]
young = students[0]

for i in range(1, N):

    name, d, m, y = students[i]
    # 늙은놈 비교
    od, om, oy = old[1], old[2], old[3]
    # 젊은놈 비교
    yd, ym, yy = young[1], young[2], young[3]


    # 늙은놈은 빨리 태어났으니까
    if int(y) < int(oy):
        old = students[i]
    elif int(y) == int(oy):
        if int(m) < int(om):
            old = students[i]
        elif int(m) == int(om):
            if int(d) < int(od):
                old = students[i]

    # 젊은놈
    if int(y) > int(yy):
        young = students[i]
    elif int(y) == int(yy):
        if int(m) > int(ym):
            young = students[i]
        elif int(m) == int(ym):
            if int(d) > int(yd):
                young = students[i]


print(young[0])
print(old[0])