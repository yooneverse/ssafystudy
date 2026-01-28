# BAEK 15918. 랭퍼든 수열쟁이야!!
import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

# 랭퍼드 수열
# 1. 1 이상 n 이하의 자연수가 각각 두 개씩 들어 있다.
# 2. 두 개의 1 사이에는 정확히 1개의 수가 있다.
# 3. 두 개의 2 사이에는 정확히 2개의 수가 있다.
# 4. ...
# 5. 두 개의 n 사이에는 정확히 n개의 수가 있다.
# x번째 수와 y번째 수는 같다는 조건

n, x, y = map(int, input().split())

"""
3 x x x 3 x

7 x x y x x x x 7 y x x x x

y 12 y x x x x x x x x x 12 x x x x x x x x x x x
"""

fix = y - x - 1             # 고정 숫자 찾기
array = [0] * (2 * n + 1)   # 전체 배열 크기
array[x] = array[y] = fix   # 고정 자리에 숫자 넣기
visited = [False] * (n + 1)  # 넣은 숫자 체크용
visited[fix] = True         # 고정 숫자 체크
result = 0


def backtrack(cnt):
    global result
    # 전체 배열을 다 돌았으면 결과값 추가
    if cnt == 2 * n + 1:
        result += 1
        return
    # cnt 숫자가 이미 쓴 숫자이면 재귀
    if array[cnt]:
        backtrack(cnt + 1)
    else:
        for x in range(1, n + 1):
            # 넣은 숫자가 아니고 랭퍼드 수열 조건에 맞는 자리가 2n 범위 내에 있고 비어있다면 재귀
            if not visited[x] and cnt + x + 1 < 2 * n + 1 and array[cnt + x + 1] == 0:
                array[cnt] = array[cnt + x + 1] = x
                visited[x] = True
                backtrack(cnt + 1)
                visited[x] = False
                array[cnt] = array[cnt + x + 1] = 0


backtrack(1)
print(result)
