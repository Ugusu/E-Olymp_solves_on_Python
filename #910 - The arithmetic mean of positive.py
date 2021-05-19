n = int(input())
a = list(map(float, input().split()))
c = 0
s = 0
for i in range(n):
    if a[i]>0:
        s = s+a[i]
        c = c+1
if c == 0:
    print('Not Found')
else:
    print(round(s/c, 2))
