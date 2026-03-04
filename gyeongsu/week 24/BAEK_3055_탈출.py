from collections import deque

r, c = map(int, input().split())

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


field = [list(input().rstrip()) for _ in range(r)]
waterflood = [[10000] * c for _ in range(r)]
dochiway = [[-1] * c for _ in range(r)]

water = []

for ri in range(r):
    for ci in range(c):
        
        if field[ri][ci] == "D":
            end = ri, ci
        elif field[ri][ci] == "S":
            start = ri, ci
        elif field[ri][ci] == '*':
            water.append((ri, ci))
            
dochiway[start[0]][start[1]] = 0
dochi = deque([(0, start[0], start[1])]) # dochi는 cnt, r, c

wq = deque([])


for i in range(len(water)):
    cr, cc = water[i][0], water[i][1]
    wq.append((0, cr, cc))
    waterflood[cr][cc] = 0

# 두가지 방법이 있따

# 1. 물 bfs 먼저 다돌리고 dochi cnt가 낮은 곳만 지나가기

# 2. 동시에 돌리기 동시에 돌리는게 훨 저렴할거 같은데


# 1이 더 쉬운듯.


while wq:
    
    cnt, cr, cc = wq.popleft()
    
    

    
    for i in range(4):
        nr, nc = cr + dr[i], cc + dc[i]
        
        if (0 <= nr < r and 0 <= nc < c and not field[nr][nc] in 'XD'):
            
            if waterflood[nr][nc] != 10000:
                continue
            
            waterflood[nr][nc] = cnt + 1
            wq.append((cnt + 1, nr, nc))
            

while dochi:
    
    cnt2, cr, cc = dochi.popleft()
    # print(cr, cc, cnt2)
    if cr == end[0] and cc == end[1]:
        print(cnt2)
        break
    
    for i in range(4):
        nr, nc = cr + dr[i], cc + dc[i]
        
        if (0 <= nr < r and 0 <= nc < c and not field[nr][nc] == 'X'):
            
            if dochiway[nr][nc] != -1: continue
            
            if waterflood[nr][nc] <= cnt2 + 1: continue
            
            dochiway[nr][nc] = cnt2 + 1
            dochi.append((cnt2 + 1, nr, nc))

else:
    print("KAKTUS")

# for bb in dochiway:
#     print(*bb)

# print('---------')
# for aa in waterflood:
#     print(*aa)

    
    
    
    