a = int(input())
b = list(map(int,input().split()))
b.sort()
cnt = 0
arr = []
for i in b:
    cnt += i
    arr.append(cnt)
print(sum(arr))