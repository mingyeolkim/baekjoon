arr = []
for i in range(100):
    arr11 = []
    for j in range(100):
        arr11.append(0)
    arr.append(arr11)
    
# arr = [[0 for j in range(100)] for i in range(100)]
        
n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            arr[i][j] = 1
rst = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            rst += 1
print(rst)