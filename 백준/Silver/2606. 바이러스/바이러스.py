
n = int(input())
k = int(input())

arr = [[] for i in range(n+1)]
visited = [0] * (n+1)

for i in range(k):
    a,b = map(int,input().split())
    arr[a] = arr[a]+ [b]
    arr[b] = arr[b]+ [a]

def dfs(v):
    visited[v] = 1
    for j in arr[v]:
        if visited[j] == 0:
            dfs(j)
dfs(1)
print(sum(visited)-1)