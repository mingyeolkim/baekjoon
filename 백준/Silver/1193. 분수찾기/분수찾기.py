a = int(input())
cnt = 1
b = 0
while a > cnt:
    a -= cnt
    cnt += 1
    b += 1
arr = []
if b % 2 != 0:
    for i in range(1,cnt+1):
        arr.append(str(i)+'/'+str(cnt-i+1))
else:
    for i in range(1,cnt+1):
        arr.append(str(cnt-i+1)+'/'+str(i))
print(arr[a-1])