T = int(input())

for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    eat = 0

    # Step 1: B < C
    if B >= C:
        eat += B - (C - 1)   # 먹은 개수
        B = C - 1            # B를 줄임
    if B < 1:                # 비어버리면 실패
        print(f"#{tc} -1")
        continue

    # Step 2: A < B
    if A >= B:
        eat += A - (B - 1)
        A = B - 1
    if A < 1:
        print(f"#{tc} -1")
        continue

    print(f"#{tc} {eat}")


