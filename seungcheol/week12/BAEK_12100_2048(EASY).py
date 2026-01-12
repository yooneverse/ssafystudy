import sys
input = sys.stdin.readline

# 최초 풀이
# def tzfe(cnt, numbers):
#     global result
#     if cnt == 5:
#         for i in range(N):
#             for j in range(N):
#                 result = max(numbers[i][j], result)
#         return
#
#     for i in range(4):
#         tmp = [[0] * N for _ in range(N)]
#         if i % 2:
#             for idx in range(N):
#                 write = plus = start[i][0]
#                 step = start[i][1]
#                 nxt = plus + step
#                 while 0 <= plus < N:
#                     if plus != start[i][0] and (plus == N - 1 or plus == 0):
#                         pass
#                     elif not numbers[idx][plus]:
#                         plus = nxt
#                         nxt += step
#                         continue
#                     elif nxt != start[i][0] and (nxt == N - 1 or nxt == 0) and not numbers[idx][nxt]:
#                         pass
#                     elif 0 <= nxt < N and not numbers[idx][nxt]:
#                         nxt += step
#                         continue
#                     if plus != start[i][0] and (plus == N - 1 or plus == 0):
#                         tmp[idx][write] = numbers[idx][plus]
#                         plus += step
#                     elif 0 <= nxt < N and numbers[idx][plus] == numbers[idx][nxt]:
#                         tmp[idx][write] = 2 * numbers[idx][plus]
#                         plus = nxt + step
#                         nxt = plus + step
#                     elif 0 <= nxt < N and numbers[idx][plus] != numbers[idx][nxt]:
#                         tmp[idx][write] = numbers[idx][plus]
#                         plus = nxt
#                         nxt += step
#                     write += step
#         else:
#             for idx in range(N):
#                 write = plus = start[i][0]
#                 step = start[i][1]
#                 nxt = plus + step
#                 while 0 <= plus < N:
#                     if plus != start[i][0] and (plus == N - 1 or plus == 0):
#                         pass
#                     elif not numbers[plus][idx]:
#                         plus = nxt
#                         nxt += step
#                         continue
#                     elif nxt != start[i][0] and (nxt == N - 1 or nxt == 0) and not numbers[nxt][idx]:
#                         pass
#                     elif 0 <= nxt < N and not numbers[nxt][idx]:
#                         nxt += step
#                         continue
#                     if plus != start[i][0] and (plus == N - 1 or plus == 0):
#                         tmp[write][idx] = numbers[plus][idx]
#                         plus += step
#                     elif 0 <= nxt < N and numbers[plus][idx] == numbers[nxt][idx]:
#                         tmp[write][idx] = 2 * numbers[plus][idx]
#                         plus = nxt + step
#                         nxt = plus + step
#                     elif 0 <= nxt < N and numbers[plus][idx] != numbers[nxt][idx]:
#                         tmp[write][idx] = numbers[plus][idx]
#                         plus = nxt
#                         nxt += step
#                     write += step
#         tzfe(cnt + 1, tmp)
#
# N = int(input())
# grid = [list(map(int, input().split())) for _ in range(N)]
#
# start = ((0, 1), (0, 1), (N - 1, -1), (N - 1, -1))
#
# result = 0
# if N == 1:
#     result = grid[0][0]
# else:
#     tzfe(0, grid)
#
# print(result)


def slide(idx, numbers):
    for i in range(N):
        if idx == 0:
            line = numbers[i]
            merge_line = merge(line)
            numbers[i] = merge_line
        elif idx == 1:
            line = [numbers[j][i] for j in range(N)]
            merge_line = merge(line)
            for j in range(N):
                numbers[j][i] = merge_line[j]
        elif idx == 2:
            line = numbers[i]
            merge_line = merge(line, True)
            numbers[i] = merge_line
        else:
            line = [numbers[j][i] for j in range(N)]
            merge_line = merge(line, True)
            for j in range(N):
                numbers[j][i] = merge_line[j]
    return numbers

def merge(line, reverse=False):
    original = []
    if reverse:
        line = line[::-1]

    for x in line:
        if x:
            original.append(x)

    merge_line = [0] * N
    idx = N - 1
    while original:
        num = original.pop()
        if merge_line[idx] == 0:
            merge_line[idx] = num
        elif merge_line[idx] == num:
            merge_line[idx] += num
            idx -= 1
        else:
            idx -= 1
            merge_line[idx] = num

    if reverse:
        merge_line = merge_line[::-1]
    return merge_line

def solve(cnt, numbers):
    global result
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                result = max(numbers[i][j], result)
        return
    for i in range(4):
        tmp = [numbers[x][:] for x in range(N)]
        tmp = slide(i, tmp)
        solve(cnt + 1, tmp)

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

result = 0

solve(0, grid)

print(result)
