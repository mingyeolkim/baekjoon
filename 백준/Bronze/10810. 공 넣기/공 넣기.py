n, m = map(int,input().split())
arr=[0]*n
for i in range(m):
    i,j,k = map(int,input().split())
    for x in range(i-1,j):
        del arr[x]
        arr.insert(x,k)
for i in arr:
    print(i,end=' ')