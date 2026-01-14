S = input()
T = input()

while len(S) != len(T):
    last = T[-1]
    if last == 'A':
        T = T[:-1]
    else:
        T = T[:-1]
        T = T[::-1]

if S == T:
    print(1)
else:
    print(0)