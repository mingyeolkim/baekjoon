import sys
input = sys.stdin.readline
n = int(input())
arr = []
ans = []
cnt = 1
for i in range(n):
    a = int(input())
    while cnt <= a:
        arr.append(cnt)
        ans.append('+')
        cnt += 1
    if arr[-1] == a:
        arr.pop()
        ans.append('-')        
    else:
        print('NO')
        break

if len(arr) == 0:
    for i in ans:
        print(i)