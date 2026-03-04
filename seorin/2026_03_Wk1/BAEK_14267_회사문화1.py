n,m = map(int,input().split()) # 직원 수 / 칭찬 횟수 
superior = list(map(int,input().split()))
result = [0] * (n+1) # 최종 칭찬 점수 

# 직접 받은 칭찬 점수 먼저 저장
for _ in range(m):
    i,w = map(int,input().split())
    result[i] += w

# 자신의 상사의 누적 칭찬을 더해줌
for i in range(2,n+1):
    result[i] += result[superior[i-1]]    
    
print(*result[1:])