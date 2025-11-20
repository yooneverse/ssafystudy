N = int(input())
buttons = [0] + list(map(int, input().split()))
S = int(input())
students = []

for _ in range(S):
    a, b = map(int, input().split())

    # 남학생이라면
    if a == 1:
        # 배수를 찾아야 함
        for i in range(b, N+1, b):
            buttons[i] = 1 - buttons[i]

    # 여학생이라면
    else:
        buttons[b] = 1 - buttons[b]

        left = b -1
        right = b +1

        while left >= 1 and right <= N and buttons[left] == buttons[right]:
            # 둘 다 반전
            buttons[left] = 1 - buttons[left]
            buttons[right] = 1 - buttons[right]

            # 다음 번호 탐색하기
            left -= 1
            right += 1

# 한 줄에 20개씩 출력해야 함
for i in range(1, N + 1):
    print(buttons[i], end=' ')
    if i % 20 == 0:
        print()