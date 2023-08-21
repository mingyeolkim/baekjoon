n = int(input())
arr = []
cnt = 0
for _ in range(n):
    a = input()
    arr.append(a)
for i in arr:
    for j in range(len(i) - 1):
        if i[j] == i[j+1]:
            pass
        elif i[j] in i[j+1:]:
            cnt += 1
            break
print(n - cnt)
