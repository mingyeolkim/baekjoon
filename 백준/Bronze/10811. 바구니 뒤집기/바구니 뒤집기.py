import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(i+1)
    
for i in range(m):
    a,b = map(int,input().split())
    arr1 = arr[a-1:b]
    arr1.reverse()
    arr[a-1:b] = arr1
for i in arr:
    print(i,end=' ')