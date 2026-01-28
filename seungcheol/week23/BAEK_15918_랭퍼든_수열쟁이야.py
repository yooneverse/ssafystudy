"""
정해진 조건
1. 1이상 n 이하의 자연수가 각각 2개씩 들어있다.
1-1. 1에 따라서 수열의 길이는 2 * n
2. 두개의 1 사이에는 정확히 1개의 수가 있다
2-1. 두개의 n 사이에는 정확히 n개의 수가 있다.
3. 주어진 입력값 x, y의 위치의 수는 같다
3-1. arr[x-1] = arr[y-1] = y - x - 1
"""
import sys

input = sys.stdin.readline

# 수열에 들어있는 최대값, 정해진 값 위치1, 2
n, x, y = map(int, input().split())

# 랭퍼드 수열이 들어갈 리스트
arr = [0] * 2 * n

# 사용한 자연수를 기록하기 위한 visited
visited = [0] * (n + 1)

# 조건 3에 의하여 값 저장하고 시작
tmp = y - x - 1
arr[x - 1] = tmp
arr[y - 1] = tmp
visited[tmp] = 1

# 랭퍼드 수열을 구하는 재귀함수
def lang(idx):
    global answer

    # idx가 2n이라는 것은
    # 아래의 조건식 및 반복문에 의해 arr이 자연수로 가득 채워졌다는 의미
    if idx == 2 * n:
        answer += 1
        return

    # 현재 인덱스가 자연수라면 다음 인덱스로 이동
    if arr[idx]:
        lang(idx + 1)
        return

    # 1부터 n까지의 자연수를 확인
    for i in range(1, n + 1):
        # i를 사용했다면 다음 자연수를 확인
        if visited[i]:
            continue

        # 현재 인덱스에서 i + 1을 더한 인덱스가 범위 안이고
        # 그 값이 0이라면
        if idx + i + 1 < 2 * n and not arr[idx + i + 1]:
            # 정보 저장
            arr[idx] = i
            arr[idx + i + 1] = i
            visited[i] = 1

            # 다음 인덱스로 이동
            lang(idx + 1)

            # 정보 롤백
            arr[idx] = 0
            arr[idx + i + 1] = 0
            visited[i] = 0

# 조건을 만족하는 랭퍼드 수열의 개수
answer = 0

# index 0부터 시작
lang(0)

print(answer)
