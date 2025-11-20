# N을 1, 2, 3의 합으로 나타내는 경우의 수를 구하기

def count_ways(n):
    # 1 만들기
    # 1 : 한 가지
    if n == 1:
        return 1

    # 2 만들기
    # (1+1), (2) : 두 가지
    elif n == 2:
        return 2

    # 3 만들기
    # (1+1+1), (1+2), (2+1), (3) : 네 가지
    elif n == 3:
        return 4

    # (n-1에 1을 더한 경우) + (n-2에 2를 더한 경우) + (n-3에 3을 더한 경우)
    else:
        return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)


T = int(input())

for _ in range(T):
    n = int(input())
    print(count_ways(n))
