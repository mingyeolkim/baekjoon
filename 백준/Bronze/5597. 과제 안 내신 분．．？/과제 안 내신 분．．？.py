arr=[]
for i in range(1,31):
    arr.append(i)
for _ in range(28):
    a = int(input())
    arr.remove(a)
print(min(arr))
print(max(arr))