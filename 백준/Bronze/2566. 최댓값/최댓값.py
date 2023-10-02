arr = []
for i in range(9):
    a =list(map(int,input().split()))
    arr.append(a)
max = 0
a = 0
b = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] > max:
            max = arr[i][j]
            a = i
            b = j
        else:
            continue
print(max)
print(a+1,b+1)