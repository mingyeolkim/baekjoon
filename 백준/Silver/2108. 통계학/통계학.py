import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)
def mycount(arr):
    dic = {}
    for i in arr:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    mv = max(dic.values())
    mvlist = []

    for i in dic:
        if mv == dic[i]:
            mvlist.append(i)
    if len(mvlist) > 1:
        return mvlist[1]
    else:
        return mvlist[0]


print(round(sum(arr)/len(arr)))
arr.sort()
print(arr[n//2])
print(mycount(arr))
print(max(arr) - min(arr))