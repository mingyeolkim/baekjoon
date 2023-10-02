dic = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}

arr = []
arr1 = []
for i in range(20):
    a,b,c = map(str,input().split())
    if c != 'P':
        arr.append(float(b)*dic[c])
    else:
        continue
    arr1.append(float(b))
grade = sum(arr)/sum(arr1)
print('%.6f' % grade)