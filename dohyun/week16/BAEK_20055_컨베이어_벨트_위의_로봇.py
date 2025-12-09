# BAEK 20055. 컨베이어 벨트 위의 로봇
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 컨베이어 벨트 길이: N, 벨트 길이: 2N
N, K = map(int, input().split())

# 벨트가 한 칸 회전하면 1번부터 2N-1번까지의 칸은 다음 번호의 칸이 있는 위치로 이동하고, 2N번 칸은 1번 칸의 위치로 이동
# i번 칸의 내구도는 Ai, 1번 칸이 있는 위치를 "올리는 위치", N번 칸이 있는 위치를 "내리는 위치"

# 로봇은 컨베이어 벨트 위에서 스스로 이동할 수 있다
# 로봇을 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 1만큼 감소

# 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
# 2-1. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
# 2-2. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
# 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
# 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.

# 종료되었을 때 몇 번째 단계가 진행 중이었는지, 가장 처음 수행되는 단계는 1번째 단계


# # belt_idx: 올리는 위치
# def move_belt(belt_idx, turn):
#     # 내구도가 0인 칸의 개수가 K개 이상이면 과정 종료
#     if A.count(0) >= K:
#         return turn - 1
#
#     # 로봇 얹기
#     if not on_robot[belt_idx] and A[belt_idx]:
#         on_robot[belt_idx] = True
#         A[belt_idx] -= 1
#         # 내구도가 0인 칸의 개수가 K개 이상이라면 과정 종료
#         if A.count(0) == K:
#             return turn
#
#     idx = N - 2
#     # 내구도가 0인 칸의 개수가 K 보다 작고 idx 가 0 이상이면 반복
#     while A.count(0) < K and idx >= 0:
#         next_idx = (belt_idx + idx) % (N * 2)
#         if on_robot[next_idx] and not on_robot[(next_idx + 1) % (N * 2)] and A[(next_idx + 1) % (N * 2)]:
#             on_robot[next_idx] = False
#             on_robot[(next_idx + 1) % (N * 2)] = True
#             A[(next_idx + 1) % (N * 2)] -= 1
#         idx -= 1
#
#     # 내리는 위치에 로봇이 있다면 내리기
#     if on_robot[(belt_idx + N - 1) % (N * 2)]:
#         on_robot[(belt_idx + N - 1) % (N * 2)] = False
#
#     # 재귀
#     return move_belt((belt_idx - 1) % (N * 2), turn + 1)
#
#
# on_robot = [False] * (N * 2)
# print(move_belt(0, 1))
A = list(map(int, input().split()))

n = N * 2
on_robot = [False] * n
turn = belt_idx = zero_cnt = 0

while True:
    turn += 1   # 단계 증가
    belt_idx = (belt_idx - 1) % n   # 컨베이어 벨트 회전, belt_idx: 올리는 위치
    drop_idx = (belt_idx + N - 1) % n

    # 내리는 위치 비우기
    on_robot[drop_idx] = False

    # 먼저 올라간 로봇부터 앞으로 이동이 가능하면 이동
    for i in range(N-2, 0, -1):
        cur = (belt_idx + i) % n
        nxt = (cur + 1) % n
        if on_robot[cur] and not on_robot[nxt] and A[nxt]:
            on_robot[cur] = False
            on_robot[nxt] = True
            A[nxt] -= 1
            if A[nxt] == 0:
                zero_cnt += 1

    # 한 번 더 내리는 위치 비우기
    on_robot[drop_idx] = False

    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다
    if A[belt_idx]:
        on_robot[belt_idx] = True
        A[belt_idx] -= 1
        if A[belt_idx] == 0:
            zero_cnt += 1

    # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료
    if zero_cnt >= K:
        break

print(turn)
