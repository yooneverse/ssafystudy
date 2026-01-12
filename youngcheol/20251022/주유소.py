# N개의 도시
# 제일 왼쪽의 도시에서 제일 오른쪽의 도시로 자동차를 이용하여 이동

# 처음 출발시 기름 충전 후 출발
# 기름통 크기 무제한
# 각 도시마다 기름 값은 다르며
# 원안의 값 리터당 가격
# 선위의 값 거리
# 최소비용


N = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

cost = 0
min_cost = price[0]
for i in range(N-1):
    if price[i] < min_cost:
        min_cost = price[i]
    cost += min_cost * dist[i]

print(cost)