n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    c = list(map(int,input().split()))
    cnt = 0
    while b != -1:
        m = max(c)
        if c[0] == m:
            c.pop(0)
            cnt += 1
            if b == 0:
                break
            else:
                b -= 1
        else:
            
            c.append(c[0])
            c.pop(0)
            if b == 0:
                b = len(c)-1
            else:
                b -= 1
    print(cnt)