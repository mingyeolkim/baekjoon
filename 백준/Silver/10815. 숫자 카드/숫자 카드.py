import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

dic = {}
for i in b:
    dic[i] = 0
for i in a:
    if i in dic.keys():
        dic[i] = 1
for i in dic.values():
    print(i,end=' ')