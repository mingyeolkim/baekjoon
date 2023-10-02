arr = []
for i in range(5):
    a = input()
    arr.append(a)
arr1 = []
for i in range(15):
    for j in range(5):
        if i < len(arr[j]):
            arr1.append(arr[j][i])
        else:
            continue
for i in arr1:
    print(i,end='')