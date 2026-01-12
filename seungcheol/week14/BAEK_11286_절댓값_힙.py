import sys
input = sys.stdin.readline

def is_less(a, b):
    if abs(a) != abs(b):
        return abs(a) < abs(b)
    return a < b

def shift_up(heap, child):
    while child > 0:
        parent = (child - 1) // 2
        if is_less(heap[child], heap[parent]):
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent
        else:
            break

def heappush(heap, data):
    heap.append(data)

    shift_up(heap, len(heap) - 1)

def shift_down(heap, parent, last):
    while True:
        left = parent * 2 + 1
        right = parent * 2 + 2
        smallest = parent

        if left < last and is_less(heap[left], heap[smallest]):
            smallest = left
        if right < last and is_less(heap[right], heap[smallest]):
            smallest = right

        if smallest == parent:
            break

        heap[parent], heap[smallest] = heap[smallest], heap[parent]
        parent = smallest

def heappop(heap):
    if not heap:
        return 0
    elif len(heap) == 1:
        return heap.pop()

    pop_data, heap[0] = heap[0], heap.pop()
    shift_down(heap, 0, len(heap))
    return pop_data



N = int(input().strip())

heapq = []

for _ in range(N):
    x = int(input().strip())
    if x:
        heappush(heapq, x)
    else:
        print(heappop(heapq))



# # 최초 풀이
# from heapq import heappush, heappop
#
# N = int(input().strip())
# pq = []
#
# for i in range(N):
#     num = int(input().strip())
#     if num > 0:
#         heappush(pq, (num, 1))
#     elif num < 0:
#         heappush(pq, (-num, -1))
#     else:
#         if pq:
#             n, op = heappop(pq)
#             print(n * op)
#         else:
#             print(0)
