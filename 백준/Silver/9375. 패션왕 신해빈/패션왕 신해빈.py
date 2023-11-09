import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    k = int(input())
    dic = {}
    for _ in range(k):
        a,b = map(str, input().split())
        if b not in dic:
            dic[b] = 1
        else:
            dic[b] += 1
    cnt = 1
    for i in dic:
        cnt *= (dic[i]+1)
    print(cnt - 1)
