import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    a = int(input())
    arr = [0]* (a+1)
    for i in range(1,a+1):
        if i ==1:
            arr[i] = 1
        elif i == 2:
            arr[i] = 2
        elif i == 3:
            arr[i] = 4
        else:
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
    print(arr[a])
