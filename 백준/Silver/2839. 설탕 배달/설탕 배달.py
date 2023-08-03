import sys
n = int(sys.stdin.readline())
b = 0
if n % 5 == 0:
    print(n//5)
else:
    while n >=0:
        n -= 3
        b += 1
        if n%5 ==0:
            print(b+(n//5))
            break
    else:
        print(-1)