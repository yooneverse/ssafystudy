N = int(input())
# 원하는 답
count = 0

for _ in range(N):
    char = input()
    word = []
    last = ''
    group_check = True

    for c in char:
        # 이전 문자랑 다르면
        if c != last:
            if c in word:
                group_check = False
                break
            word.append(c)
        # 문자를 저장하기
        last = c

    if group_check:
        count += 1

print(count)