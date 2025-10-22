# BAEK 2661. 좋은 수열
# 백트래킹 사용
import sys
sys.stdin = open('input.txt', 'r')


def backtrack(cnt):
    a = len(ans)    # 배열 길이
    # i) 배열 길이가 홀수일 때
    if a % 2 == 1:
        # 뒤에서부터 맞대어있는 1, 2, ..., a // 2 칸씩을 비교
        for i in range(a - 1, (a // 2), -1):
            # 인접한 두 개의 부분 수열이 동일하면 가지치기
            if ans[i:] == ans[i*2-a:i]:
                return
    # ii) 배열 길이가 짝수일 때
    else:
        for i in range(a - 1, (a // 2) - 1, -1):
            if ans[i:] == ans[i*2-a:i]:
                return

    # 종료 조건
    if cnt == N:
        b = ''.join(map(str, ans))
        print(b)
        return True     # True 반환

    for i in range(1, 4):
        ans.append(i)
        # 만약 종료 조건이 활성화되었으면 True 반환
        # 끝까지 True 반환되면 함수 종료
        if backtrack(cnt + 1):
            return True
        ans.pop()


N = int(input())
ans = []

backtrack(0)
