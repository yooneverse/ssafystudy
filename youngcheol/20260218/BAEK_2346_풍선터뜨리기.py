#N개의 풍선
N = int(input())



# 종이에 적혀있는값만큼 이동하여 풍선을 터트림

#만약 이미 터져있으면 빼고 이동한다

#출력은 풍선이 순서대로 터진 순서


data = []
lst = list(map(int, input().split()))
for i in range(N):
    data.append([i + 1, lst[i]])

result = []
# 첫번째 풍선부터 터트린다
index = 0

# 오랜만에 푸니까 while도 생각이 잘 안나서... 오래걸림
while data:
    num, paper = data.pop(index)
    result.append(num)

    if not data:
        break

    #여기서는 제미나이에게 완전 도움받음 어려움...
    if paper > 0:
        index = (index + (paper - 1)) % len(data)
    else:
        index = (index + paper) % len(data)
print(*result)