'''
N 자리 자연수 중 
앞에서부터 끊은 부분 수가 모두 소수인 수

예를 들어 7331
7
73
733
7331 
모두 소수임
'''
'''
아이디어

소수 판별
N이 소수인가? N이 2부터 루트N까지의 수로 나누어 떨어지지 않으면 됨

해당 문제의 경우 부분적으로도 소수여야 하므로
가장 앞 자리수만 2 가능, 나머지도 3,5,7 만 가능

앞에서부터 소수인지 확인
끝까지 모두 소수라면 출력

소수 하나 가져와서 뒤에 숫자 하나씩 붙이면서 소수인지 확인
'''

import math

def isPrime(n):
    if n < 2:
        return False
    last = int(math.sqrt(n))
    for num in range(2,last+1):
        if n%num == 0:
            return False

    return True

def dfs(num):
    if len(str(num))==N:
        print(num)
        return

    for i in range(1,10):
        if i%2 == 0:
            continue

        next_num = num *10 +i
        if isPrime(next_num):
            dfs(next_num)

N = int(input())

for start in [2,3,5,7]:
    dfs(start)