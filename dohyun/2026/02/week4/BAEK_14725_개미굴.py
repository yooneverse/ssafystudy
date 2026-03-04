# BAEK 14725. 개미굴
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())


# 입력 함수
# trie: 루트 노드(입력값이 빈 dict), path: 먹이 찾아 내려간 순서대로 입력
def insert(trie, path):
    node = trie
    for key in path:
        # 만약 먹이가 중복되지 않으면 빈 딕셔너리로 자식 노드 생성
        if key not in node:
            node[key] = {}
        # 자식 노드로 이동
        node = node[key]


# 출력 함수
# node: 현재 보고 있는 노드, depth: 현재 지하 층 수
def print_trie(node, depth):
    # for문에서 keys를 정렬하여 출력
    # 만약 빈 딕셔너리(최하층)에 도달하면 node.keys()가 없으므로 재귀 종료됨
    for key in sorted(node.keys()):
        print('--' * depth + key)
        print_trie(node[key], depth + 1)


trie = {}
for _ in range(N):
    info = list(map(str, input().split()))
    insert(trie, info[1:])

print_trie(trie, 0)
