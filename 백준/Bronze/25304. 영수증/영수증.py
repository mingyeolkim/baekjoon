n = int(input())
c = int(input())
price = 0
for i in range(c):
    a,b = map(int,input().split())
    price += a*b
if price == n:
    print('Yes')
else:
    print('No')