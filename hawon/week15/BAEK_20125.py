N = int(input())
lst = list((input().strip()) for _ in range(N))

hr, hc = -1, -1
found = False

for r in range(N):
    for c in range(N):
        if lst[r][c] == '*':
            hr, hc = r, c
            found = True
            break
    if found:
        break

heart_r = hr + 1
heart_c = hc

print(heart_r+1, heart_c+1)

# 3. 왼팔 길이
left_arm = 0
c = heart_c - 1
while c >= 0 and lst[heart_r][c] == '*':
    left_arm += 1
    c -= 1

# 4. 오른팔 길이
right_arm = 0
c = heart_c + 1
while c < N and lst[heart_r][c] == '*':
    right_arm += 1
    c += 1

# 5. 허리 길이
waist = 0
r = heart_r + 1
while r < N and lst[r][heart_c] == '*':
    waist += 1
    r += 1

waist_end_r = heart_r + waist

# 6. 왼다리 길이
left_leg = 0
r = waist_end_r + 1
c = heart_c - 1
while r < N and c >= 0 and lst[r][c] == '*':
    left_leg += 1
    r += 1

# 7. 오른다리 길이
right_leg = 0
r = waist_end_r + 1
c = heart_c + 1
while r < N and c < N and lst[r][c] == '*':
    right_leg += 1
    r += 1


print(left_arm, right_arm, waist, left_leg, right_leg)