a = list(map(int,input().split()))
arr = [1,1,2,2,2,8]
arr1 = []
for i in range(len(a)):
    arr1.append(arr[i] - a[i])
for i in arr1:
    print(i,end=' ')