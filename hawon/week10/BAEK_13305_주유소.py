# 1km마다 1리터의 기름을 사용
N = int(input()) # 도시 개수
road = list(map(int, input().split())) # 도로의 길이
charge = list(map(int, input().split())) # 주유소 리터당 가격

# 총 가격
total = 0
# 첫번째 가격을 제일 작은 가격으로 설정
min_price = charge[0]

# 지금 있는 곳보다 다음곳이 더 싸다면, 다음 곳으로 갱신
# 첫번째 도시는 아묻따 가야함
for i in range(N-1):
    if charge[i] < min_price:
        min_price = charge[i]
    total += min_price * road[i]

print(total)