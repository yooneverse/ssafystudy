# BAEK 22251. 빌런 호석
import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# N: 최대 층 수, K: LED 칸 수, P: 최대 반전 횟수, X: 현재 층 수
N, K, P, X = map(int, input().split())

# 숫자를 전부 표현하면 되지 않을까
numbers = {
0: [True, True, True, False, True, True, True],
1: [False, False, True, False, False, True, False],
2: [True, False, True, True, True, False, True],
3: [True, False, True, True, False, True, True],
4: [False, True, True, True, False, True, False],
5: [True, True, False, True, False, True, True],
6: [True, True, False, True, True, True, True],
7: [True, False, True, False, False, True, False],
8: [True, True, True, True, True, True, True],
9: [True, True, True, True, False, True, True]
}

# 숫자 비교를 어떻게 하지?
# 문자열로 바꿔서 자릿수마다 비교
result = 0
# zfill(K): 0을 모자란 만큼 추가해 K자리의 문자열로 만들어줌.
str_X = str(X).zfill(K)

for i in range(1, N+1):
    # 같은 수일 때는 스킵
    if i == X:
        continue
    str_i = str(i).zfill(K)
    cnt = j = 0
    # 자릿수마다 7-세그먼트 비교
    while True:
        if j >= K or cnt > P:
            break
        lst = numbers[int(str_X[j])]
        comp_lst = numbers[int(str_i[j])]
        idx = 0
        while cnt <= P and idx < 7:
            if lst[idx] != comp_lst[idx]:
                cnt += 1
            idx += 1
        j += 1
    if cnt <= P:
        result += 1

print(result)
