import sys
input = sys.stdin.readline
n = int(input())
s = set()
for _ in range(n):
    a = input().split()
    if len(a) == 1:
        a0 = a[0]
    else:
        a0,a1 = a
    if a0 == 'add':
        s.add(int(a1))
    elif a0 == 'remove':
        if int(a1) in s:
            s.discard(int(a1))
    elif a0 == 'check':
        if int(a1) in s:
            print(1)
        else:
            print(0)
    elif a0 == 'toggle':
        if int(a1) not in s:
            s.add(int(a1))
        else:
            s.discard(int(a1))
    elif a0 == 'all':
        s = {1,2,3,4,5,6,7,8,9,10,
             11,12,13,14,15,16,17,18,19,20}
    elif a0 == 'empty':
        s = set()  