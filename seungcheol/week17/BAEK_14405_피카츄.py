import sys
input = sys.stdin.readline

sentence = input().strip()

idx = 0
length = len(sentence)
flag = True

while idx < length:
    if idx + 1 < length and sentence[idx] == "p" and sentence[idx + 1] == "i":
        idx += 2
        continue
    elif idx + 1 < length and sentence[idx] == "k" and sentence[idx + 1] == "a":
        idx += 2
        continue
    elif idx + 2 < length and sentence[idx] == "c" and sentence[idx + 1] == "h" and sentence[idx + 2] == "u":
        idx += 3
        continue
    else:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
