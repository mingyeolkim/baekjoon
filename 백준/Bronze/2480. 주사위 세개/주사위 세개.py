a = list(map(int,input().split()))
if len(set(a)) == 1:
    print(10000+a[0]*1000)
elif len(set(a)) == 2:
    q = a[0]*100 + 1000
    w = a[1]*100 + 1000
    e = a[2]*100 + 1000
    if q == w or q == e:
        print(q)
    elif w == e:
        print(w)
    
else:
    print(max(a)*100)