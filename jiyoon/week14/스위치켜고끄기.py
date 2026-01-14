# 스위치 개수 입력
N = int(input())

# 스위치 상태 입력 (인덱스 1부터 쓰기 위해 앞에 0 추가)
switches = [0] + list(map(int, input().split()))

# 학생 수 입력
students = int(input())

# 스위치를 반전시키는 함수 (0 → 1, 1 → 0)
def toggle(i):
    switches[i] = 1 - switches[i]

# 학생 수만큼 스위치 조작 반복
for _ in range(students):
    gender, num = map(int, input().split())  # 성별, 받은 숫자 입력

    if gender == 1:  # 남학생인 경우
        for i in range(num, N + 1, num):     # num 배수 위치 모두 반전
            toggle(i)

    else:  # 여학생인 경우
        toggle(num)                          # 우선 본인 위치 반전
        left = num - 1                       # 왼쪽 번호 확인
        right = num + 1                      # 오른쪽 번호 확인

        # 좌우가 범위를 넘지 않고, 값이 같으면 계속 확장하며 반전
        while left >= 1 and right <= N and switches[left] == switches[right]:
            toggle(left)
            toggle(right)
            left -= 1                        # 왼쪽 번호로 이동
            right += 1                       # 오른쪽 번호로 이동

# 스위치 상태를 20개씩 끊어서 출력
# *** 이 부분이 스스로 생각해내기 어려웠습니다. 혼자서 어떻게 20개를 뽑아낼지 몰라 힌트를 얻었습니다.
for i in range(1, N + 1):
    print(switches[i], end=' ')              # *** 스위치 상태 출력
    if i % 20 == 0:                          # *** 20개 출력할 때마다 줄바꿈 _ 이 부분 복습하기!
        print()
