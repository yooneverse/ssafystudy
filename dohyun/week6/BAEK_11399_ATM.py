# BAEK 11399. ATM
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
P = list(map(int, input().split()))

P.sort()    # 배열 오름차순 정렬
sum_time = 0    # 기다린 시간 더할 변수
for i in range(N):
    # 남은 인원수 만큼 기다리는 시간 곱해서 저장
    sum_time += P[i] * (N - i)

print(sum_time)
