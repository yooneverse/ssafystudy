#길이가 N인 정수 배열 A와 B


# S = A[0] × B[0] + ... + A[N-1] × B[N-1]

# S의 값을 가장 작게 만들기 위하여 A의 수 재배열

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()

B.sort(reverse=True)

S = 0
for i in range(N):
    S += A[i] * B[i]

print(S)

        




