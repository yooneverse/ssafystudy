N = int(input())                           # 도시 수
roads = list(map(int, input().split()))    # 도로 길이 입력
prices = list(map(int, input().split()))   # 기름 값 입력

total = 0                # 지금까지 쓴 돈   
min_price = prices[0]    # 지금까지 최소 비용

for i in range(N - 1):               # N 개의 도시까지의 비용 구하기 위해 진행
    total += min_price * roads[i]    # 총 비용은 최소 가격 * 도로 길이 합
    if prices[i + 1] < min_price:    # 최소 가격보다 작은 가격이 다음에 발견하면
        min_price = prices[i + 1]    # 최소 가격 바꿈

print(total)                         
