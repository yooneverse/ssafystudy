origin = input()
goal = input()

flag = False

o_len = len(origin)
g_len = len(goal)


while True:
    if g_len == o_len:
        if goal == origin:
            flag = True
        break
    g_len -= 1
    if goal[g_len] == "A":
        goal = goal[:g_len]
    else:
        goal = goal[:g_len]
        goal = goal[::-1]

if flag:
    print(1)
else:
    print(0)

