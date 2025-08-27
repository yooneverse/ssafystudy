N = int(input())

# 설탕 N kg 을 3kg과 5kg로 나눴을때
# 나머지가 0이 나와야한다.

count = 0
while N >= 0:
    if N % 5 == 0: # 봉지의 최솟값을 위해 N을 5로 먼저 나누고
        count += N//5 # 만약 나머지가 0이면 그대로 출력
        print(count)
        break
    N -= 3   # 5로 나누어 지지 않으면 3을 하나씩 빼서 횟수에 1회씩 추가
    count += 1
else:
    print(-1) 
    # 3이랑 5랑 나눠지지 안된다면 -1로 출력