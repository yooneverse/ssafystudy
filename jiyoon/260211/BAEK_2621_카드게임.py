# 카드 색과 숫자를 저장할 리스트
color_list = []
number_list = []

# 숫자 개수를 세기 위한 리스트 (인덱스 1~9 사용)
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 카드 5장 입력
for i in range(5):
    # 색과 숫자를 문자열로 입력받음
    c, n = input().split()

    # 숫자는 계산해야 하니까 정수로 바꿔줌
    n = int(n)

    # 각각 리스트에 저장
    color_list.append(c)
    number_list.append(n)

    # 해당 숫자의 개수 +1
    count[n] = count[n] + 1


# 숫자 리스트 정렬 (연속인지 확인하려고)
number_list.sort()

# 가장 큰 숫자
max_num = number_list[4]

# 가장 작은 숫자
min_num = number_list[0]


# -----------------------------
# 색이 전부 같은지 확인
# -----------------------------
same_color = True

# 첫 번째 색이랑 나머지 색 비교
for i in range(1, 5):
    if color_list[i] != color_list[0]:
        same_color = False


# -----------------------------
# 숫자가 연속인지 확인
# -----------------------------
is_straight = True

# 앞 숫자 + 1 == 다음 숫자 인지 확인
for i in range(4):
    if number_list[i] + 1 != number_list[i + 1]:
        is_straight = False


# -----------------------------
# 같은 숫자가 몇 개 있는지 확인
# -----------------------------
# 가장 많이 나온 개수
max_count = 0

for i in range(1, 10):
    if count[i] > max_count:
        max_count = count[i]


# -----------------------------
# 점수 계산 시작
# (문제 조건 순서대로 위에서부터 검사)
# -----------------------------

# 1. 같은 색 + 연속
if same_color == True and is_straight == True:
    score = 900 + max_num

# 2. 같은 숫자 4개
elif max_count == 4:
    for i in range(1, 10):
        if count[i] == 4:
            score = 800 + i

# 3. 3장 + 2장 (풀하우스)
elif max_count == 3:
    three = 0
    two = 0

    for i in range(1, 10):
        if count[i] == 3:
            three = i
        if count[i] == 2:
            two = i

    if two != 0:
        score = 700 + three * 10 + two
    else:
        # 6. 같은 숫자 3개
        score = 400 + three

# 4. 같은 색만
elif same_color == True:
    score = 600 + max_num

# 5. 숫자 연속만
elif is_straight == True:
    score = 500 + max_num

# 7. 같은 숫자 2개가 두 쌍
elif max_count == 2:
    pair = []

    for i in range(1, 10):
        if count[i] == 2:
            pair.append(i)

    if len(pair) == 2:
        # 큰 숫자가 앞에 오도록 정렬
        pair.sort()
        score = 300 + pair[1] * 10 + pair[0]
    else:
        # 8. 같은 숫자 2개 한 쌍
        score = 200 + pair[0]

# 9. 아무것도 해당 안 됨
else:
    score = 100 + max_num


# 결과 출력
print(score)
