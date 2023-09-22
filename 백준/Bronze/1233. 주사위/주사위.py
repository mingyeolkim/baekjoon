a,b,c = map(int,input().split())
arr = []
for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            arr.append(i+j+k)
dic = {}
for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
mv = max(dic.values())
arr1=[]
cnt = 0
for i,j in dic.items():
    if j == mv:
        arr1.append(i)
if len(arr1) == 1:
    print(arr1[0])
else:
    print(min(arr1))