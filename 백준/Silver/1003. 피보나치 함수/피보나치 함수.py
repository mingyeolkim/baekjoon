import sys
input = sys.stdin.readline

def fib(n):
    z = [1,0,1]
    o = [0,1,1]
    if n > 2:
        for i in range(3,n+1):
            z.append(z[i-1]+z[i-2])
            o.append(o[i-1]+o[i-2])
        print(z[-1],o[-1])
    else:
        print(z[n],o[n])

T = int(input())

for i in range(T):
    a = int(input())
    fib(a)