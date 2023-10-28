n, k = map(int,input().split())
arr = []
for i in range(n):
    a = int(input())
    arr.append(a)
cnt = 0    
arr.reverse()
for i in arr:
    if i > k:
        pass
    elif i == k:
        cnt += 1
        break
    else:
        cnt += k // i
        k = k % i
print(cnt)