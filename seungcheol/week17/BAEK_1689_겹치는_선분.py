import sys
input = sys.stdin.readline

N = int(input().strip())
lines = []
for _ in range(N):
    s, e = map(int, input().split())
    lines.append((s, 1))
    lines.append((e, -1))

lines.sort(reverse=True)
answer = tmp = 0


while lines:
    _, score = lines.pop()

    tmp += score

    answer = max(answer, tmp)

print(answer)

# import sys
# input = sys.stdin.readline
#
# from heapq import heappop, heappush
#
# N = int(input().strip())
# lines = []
# for _ in range(N):
#     s, e = map(int, input().split())
#     heappush(lines, (s, 1))
#     heappush(lines, (e, -1))
#
# answer = tmp = 0
#
#
# while lines:
#     _, score = heappop(lines)
#
#     tmp += score
#
#     answer = max(answer, tmp)
#
# print(answer)
