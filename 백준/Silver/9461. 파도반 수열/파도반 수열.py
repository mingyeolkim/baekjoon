import sys
input = sys.stdin.readline

arr = [0] * (101)
arr[1] = 1
arr[2] = 1
arr[3] = 1
n = int(input())

for i in range(n):
    a = int(input())
    for i in range(4,a+1):
        arr[i] = arr[i-2] + arr[i-3]
    print(arr[a])