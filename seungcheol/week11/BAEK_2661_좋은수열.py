N = int(input())

def check(permutation):
    global answer
    if len(permutation) == N:
        answer = int(permutation)
        return

    length = len(permutation) + 1

    for i in "123":
        tmp = permutation+i
        for idx in range(1, length // 2 + 1):
            if tmp[length-2*idx:length-idx] == tmp[length-idx:]:
                break
        else:
            check(tmp)
            if answer:
                return

answer = False
check("")
print(answer)
