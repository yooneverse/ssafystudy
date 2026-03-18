N = input().strip()


cnt = [0]*10
for i in range(len(N)):
    if N[i] == '0':
        cnt[0] += 1
    elif N[i] == '1':
        cnt[1] += 1
    elif N[i] == '2':
        cnt[2] += 1
    elif N[i] == '3':
        cnt[3] += 1
    elif N[i] == '4':
        cnt[4] += 1
    elif N[i] == '5':
        cnt[5] += 1
    elif N[i] == '6':
        cnt[6] += 1
    elif N[i] == '7':
        cnt[7] += 1
    elif N[i] == '8':
        cnt[8] += 1
    elif N[i] == '9':
        cnt[9] += 1

if (cnt[6]+cnt[9])%2 == 0:
    cnt[6] = (cnt[6]+cnt[9])//2
else:
    cnt[6] = (cnt[6]+cnt[9])//2 + 1
ans = 0
for j in range(9):
    if cnt[j] > ans:
        ans = cnt[j]
print(ans)
    
    
    
        
        
