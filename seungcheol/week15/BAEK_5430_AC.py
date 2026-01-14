import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    command = input().strip()
    length = int(input().strip())
    numbers = input().strip()[1:-1]
    if numbers:
        array = list(map(int, numbers.split(',')))
    else:
        array = []

    front = 0
    rear = length
    move = 1
    for c in command:
        if c == 'R':
            move *= -1
        else:
            if front == rear:
                break
            if move == 1:
                front += move
            else:
                rear += move
    else:
        print('[', end='')
        if move == 1:
            for idx in range(front, rear):
                if idx != rear-1:
                    print(array[idx], end=',')
                else:
                    print(array[idx], end='')
        else:
            for idx in range(rear - 1, front - 1, -1):
                if idx != front:
                    print(array[idx], end=',')
                else:
                    print(array[idx], end='')
        print(']')
        continue
    print('error')
