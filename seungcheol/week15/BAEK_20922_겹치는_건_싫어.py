import sys
input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())

    numbers = list(map(int, input().split()))

    check = {}
    answer = 0

    front = rear = 0
    while rear < N:
        check[numbers[rear]] = check.get(numbers[rear], 0) + 1

        while check[numbers[rear]] > K:
            check[numbers[front]] -= 1
            front += 1
        rear += 1
        answer = max(answer, rear - front)

    print(answer)

if __name__ == '__main__':
    solve()
