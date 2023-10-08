n, m = map(int,input().split())
dic = {}
arr1 = []
for i in range(n):
    a = input().split()
    dic[a[0]] = a[1]
for i in range(m):
    a = input()
    arr1.append(a)
for i in arr1:
    print(dic[i])