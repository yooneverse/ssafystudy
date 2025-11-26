N, M = map(int, input().split())

heard = set()

for _ in range(N):
    name = input()
    heard.add(name)

result = []

for _ in range(M):
    name = input()
    if name in heard:
        result.append(name)

result.sort()

print(len(result))       
print("\n".join(result)) 
