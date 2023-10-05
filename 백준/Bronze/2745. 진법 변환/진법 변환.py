a,b = map(str,input().split())
cnt = 0
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(a)):
    cnt += number.index(a[-i-1]) * int(b)**i
print(cnt)