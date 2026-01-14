# BAEK 1700. 멀티탭 스케줄링
import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 플러그를 빼는 횟수를 최소화하는 방법
# 멀티탭: set, 사용 순서: deque

N, K = map(int, input().split())
order = deque(list(map(int, input().split())))
plug = set()
cnt = 0

while order:
    next = order.popleft()  # 다음 순서 빼내기
    # 빈 플러그가 있거나 다음 순서인 장치가 이미 꽂혀있다면 set에 추가
    if len(plug) < N or next in plug:
        plug.add(next)
    else:
        last_idx = -1   # 순서상 가장 뒤에 위치한 기기의 idx
        for item in plug:
            # 만약 플러그에 꽂혀있는 제품이 남은 순서에 있다면 idx 비교
            if item in order:
                idx = list(order).index(item)
                if idx > last_idx:
                    last_idx = idx
                    to_remove = item
            else:
                # 다시 사용 안되는 제품이 나오면 바로 뺌
                to_remove = item
                break
        plug.discard(to_remove)
        plug.add(next)
        cnt += 1

print(cnt)
