def factorial(n):
    if n >= 1:
        return n * factorial(n-1)
    else:
        return 1
    
n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    ans = factorial(b) // (factorial(b-a) * factorial(a))
    print(ans)