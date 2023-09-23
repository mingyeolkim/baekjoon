import sys
input = sys.stdin.readline
x = 1
n = int(input())
for i in range(n):
    a = input().split()
    arr = []
    arr1 = []
    for i in a:
        arr.append(i)
    for i in range(len(arr)):
        arr1.append(arr.pop())
    print(f'Case #{x}:',end=' ')
    for i in arr1:
        print(i,end=' ')
    print()
    x += 1