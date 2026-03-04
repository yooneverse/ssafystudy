# 봄 : 자신의 나이만큼 양분을 먹고 나이가 증가
    # 어린나무 부터 섭취
    # 충분히 못먹으면 사망
    
# 여름 : 죽은 나무가 양분화 됨 나무 나이 / 2
# 가을 : 나무 번식 8칸에 번식함
# 겨울 : 양분 추가

from collections import deque

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
yangboon = [[5] * n for _ in range(n)]
die = [[0] * n for _ in range(n)]

# 3차원 배열로 할까  [r][c] = [트리정보1, 트리정보2]
trees = [[deque([]) for _ in range(n)] for _ in range(n)]


for _ in range(m):
    r, c, age = map(int, input().split()) # 1 base 입력
    trees[r-1][c-1].append(age) # 0 base 저장
    # print(age)
    
def init():
    
    for r in range(n):
        for c in range(n):
            
            if trees[r][c]:
                trees[r][c] = deque(sorted(trees[r][c]))

init()
# print(trees)
def spring():
    
    for r in range(n):
        for c in range(n):
            
            
            tlist = trees[r][c]
            
            # print(tlist)
            for i in range(len(tlist)):
                
                tree = tlist.popleft()
                
                if tree <= yangboon[r][c]: # 먹을 양분이 남아 있는경우 데크로 구현하는게 나을듯
                    yangboon[r][c] -= tree
                    tlist.append(tree + 1)
                    
                else:
                    die[r][c] += tree // 2
                    
            # print(tlist)
            
def summer():
    
    for r in range(n):
        for c in range(n):
            
            yangboon[r][c] += die[r][c]
            die[r][c] = 0
            

def falling():
    
    for r in range(n):
        for c in range(n):
            
            for t in trees[r][c]:
                if t % 5 == 0:
                    
                    # 번식 로직
                    
                    for dr in range(-1,2,1):
                        for dc in range(-1,2,1):
                            if dr == 0 and dc == 0: continue
                        
                            nr, nc = r + dr, c + dc
                            
                            if (0 <= nr < n and 0 <= nc < n):
                                
                                trees[nr][nc].append(1)
                                

def winter():
    
    for r in range(n):
        for c in range(n):
            
            yangboon[r][c] += arr[r][c]


for year in range(k):

    spring()
    summer()
    falling()
    init()
    winter()


ans = 0

# for aa in trees:
#     print(*aa)
    
for r in range(n):
    for c in range(n):
        t = trees[r][c]
        
        ans += len(t)
        
print(ans)
