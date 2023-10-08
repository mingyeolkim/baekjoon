n,m = map(int,input().split())
dic = {}
arr = []
for i in range(n):
    a = input()
    dic[a] = 0
for i in range(m):
    a = input()
    if a not in dic:
        dic[a] = 0
    else:
        dic[a] += 1
for i,j in dic.items():
    if j != 0:
        arr.append(i)
arr.sort()
print(len(arr))
for i in arr:
    print(i)
