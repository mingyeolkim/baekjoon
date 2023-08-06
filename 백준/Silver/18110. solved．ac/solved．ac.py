import sys
n = int(sys.stdin.readline())
arr = []

def myround(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
    
for _ in range(n):
    a = int(sys.stdin.readline())
    arr.append(a)
arr.sort()

j = myround(n * 0.15)
if j != 0:
    arr = arr[j: -j]
if arr:
    print(myround(sum(arr)/len(arr)))
else:
    print(0)
    
#for _ in range(j):
#   arr.pop() 쓰면 시간초과가 난다
    