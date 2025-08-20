PASSWORD = 9 # 자리 수 8개, front 자리 1개
 
def enqueue(item):
    global cq, rear
    # 무조건 꽉 차 있으므로 is_full 안따짐
    rear = (rear + 1) % PASSWORD
    cq[rear] = item
 
def dequeue():
    global front
    # 배열이 빌 일이 없으므로 is_empty 안따짐
    front = (front + 1) % PASSWORD
    return cq[front]
 
T = 10
for test_case in range(1, T + 1):
    test_num = int(input())
    nums = list(map(int, input().split()))
 
    # 원형 큐 초기화
    cq = [-1] * PASSWORD
    front = rear = 0
 
    # 원형 큐 삽입
    for num in nums:
        enqueue(num)
 
    while cq[rear] != 0:
        # 사이클 돌리기
        for i in range(1, 6):
            front_num = dequeue() # 지금 자리 비울 필요 없음, 차피 덮어 씌워질거니까
            front_num -= i
            if front_num <= 0:
                front_num = 0
            enqueue(front_num)
 
            if cq[rear] == 0:
                break
                 
    if front == 0 and rear == PASSWORD - 1:
        print(f'#{test_num}', *cq[front + 1:])
    else:
        print(f'#{test_num}', *cq[front + 1:], *cq[:rear + 1])


#### 아래 코드는 이 방법으로도 제출은 가능하나
#### 강사님께서 쓰지말라고 하신 방법입니더
# T = 10
# for test_case in range(1, T + 1):
#     test_num = int(input())
#     nums = list(map(int, input().split()))
 
#     while nums[-1] != 0:
#         for i in range(1, 6):
#             front_num = nums.pop(0)
#             front_num -= i
#             if front_num <= 0:
#                 front_num = 0
#             nums.append(front_num)
 
#             if nums[-1] == 0:
#                 break
 
#     print(f'#{test_num}', *nums)