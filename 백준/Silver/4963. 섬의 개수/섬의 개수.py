import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

x = [-1,-1,-1,0,0,1,1,1]
y = [-1,0,1,-1,1,-1,0,1]

def dfs(a, b):
    global island, visited
    visited[a][b] = 1
    for dir in range(8):
        nr = x[dir] + a
        nc = y[dir] + b
        if nr >= 0 and nr < h and nc >= 0 and nc < w:
            if arr[nr][nc] == 1 and visited[nr][nc] == 0:
                dfs(nr,nc)
        
    
while 1:
    cnt = 0
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    arr = []
    visited = [[0]* w for _ in range(h)]
    for i in range(h):
        a = list(map(int,input().split()))
        arr.append(a)
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and visited[i][j] == 0:
                dfs(i,j)
                cnt += 1
    print(cnt)