arr = set()
for i in range(1,10001):
    arr.add(i)
arr2 = set()

for i in arr:
    for j in str(i):
        i = i + int(j)
    if i <= 10000:
        arr2.add(i)
arr3 = arr - arr2
for i in sorted(arr3):
    print(i)