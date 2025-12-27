'''
문제
n 가지 종류 동전, 합이 k 원 되도록 최소 동전 사용 개수 구하기
불가능할 경우 -1 출력
각 동전은 여러 번 사용 가능
동일 가치 동전이 여러 번 주어질 수도 있음
'''
'''
예를 들어
3 15
1
5
12 

15 = 12 + 1 + 1 + 1 
15 = 5 + 5 + 5 
...
최소 동전 개수는 3개가 된다
'''
'''
특정 값까지 동전의 개수를 누적 이용
>> dp
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = set()

dp = [0] + [float('inf')]*k

for _ in range(n):
    coin = int(input())
    if coin > k:
        continue
    coins.add(coin)

#coins = list(coins)
#아래 코드 추가 시 시간 20ms 줄었음
#coins.sort(reverse=True)
#큰 수부터 처리하여 수정 작업 줄임

for c in coins:
    for v in range(c,k+1):
        dp[v] = min(dp[v-c]+1, dp[v])

if dp[k] != float('inf'):
    print(dp[k])
else:
    print(-1)



