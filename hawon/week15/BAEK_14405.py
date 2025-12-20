# pi, ka, chu

S = input()
N = len(S)

i = 0
pikachu = True


while i < N:
    if i + 1 < N and (S[i] == 'p' and S[i+1] == 'i' or S[i] == 'k' and S[i+1] == 'a'):
        i += 2  
    elif i + 2 < N and S[i] == 'c' and S[i+1] == 'h' and S[i+2] == 'u':
        i += 3 
    else:
        pikachu = False
        break

if pikachu:
    print('YES')
else:
    print('NO')