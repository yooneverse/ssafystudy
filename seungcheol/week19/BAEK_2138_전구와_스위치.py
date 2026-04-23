import sys
input = sys.stdin.readline

n = int(input().strip())

# 0번 인덱스의 스위치를 on하냐 마냐에 따라 이후 스위치 클릭 여부가 정해짐
# 0번 스위치를 on한 경우
on = list(map(int, input().strip()))

# 0번 스위치를 off한 경우
off = on[:]

# 0번 스위치 on
on[0] = 1 - on[0]
on[1] = 1 - on[1]

goal = list(map(int, input().strip()))

def switch(bulb, base):
    answer = base
    for i in range(1, n - 1):
        if bulb[i - 1] != goal[i - 1]:
            bulb[i - 1] = 1 - bulb[i - 1]
            bulb[i] = 1 - bulb[i]
            bulb[i + 1] = 1 - bulb[i + 1]
            answer += 1
    if bulb[n - 2] != goal[n - 2]:
        bulb[n - 2] = 1 - bulb[n - 2]
        bulb[n - 1] = 1 - bulb[n - 1]
        answer += 1

    if bulb[n - 1] != goal[n - 1]:
        return -1
    else:
        return answer

on_answer = switch(on, 1)
off_answer = switch(off, 0)
if on_answer == off_answer == -1:
    print(-1)
elif on_answer == -1 and off_answer != -1:
    print(off_answer)
elif on_answer != -1 and off_answer == -1:
    print(on_answer)
else:
    answer = min(on_answer, off_answer)
    print(answer)
