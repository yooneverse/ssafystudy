import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    numbers = []
    flag = False

    for i in range(N):
        phone = input().strip()
        numbers.append(phone)

    numbers.sort()

    for i in range(N-1):
        left = numbers[i]
        right = numbers[i + 1]
        length = len(left)
        if left == right[:length]:
            print("NO")
            break
    else:
        print("YES")
