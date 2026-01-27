from sys import stdin

n,m = map(int,stdin.readline().split())

listen = set(str(stdin.readline().rstrip()) for _ in range(n))
see = set(str(stdin.readline().rstrip()) for _ in range(m))

result = sorted(list(listen & see))

print(len(result))
print("\n".join(result))