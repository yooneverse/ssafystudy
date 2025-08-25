def sugar(N):
    result = -1
    if 0 == N % 5:
        return N // 5
    elif 0 < N // 5:
        for i in range((N // 5) + 1):

            if 0 == (N - i * 5) % 3:
                result = i + (N - i * 5) // 3

    return result


kg = int(input())
print(sugar(kg))
