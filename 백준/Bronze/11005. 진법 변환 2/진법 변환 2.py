a, b = map(int, input().split())
arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = ''

while a:
    s += arr[a%b]
    a = a//b
print(s[::-1])