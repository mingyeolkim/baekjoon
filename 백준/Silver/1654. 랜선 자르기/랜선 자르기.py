import sys
input = sys.stdin.readline
a, b = map(int,input().split())
arr = []
for _ in range(a):
    n = int(input())
    arr.append(n)
start = 1
end = max(arr)

while start <= end:
    mid = (start + end)//2
    lan = 0
    for i in arr:
        lan += i//mid
    if lan >= b:
        start = mid +1
    else:
        end = mid -1

print(end)
    