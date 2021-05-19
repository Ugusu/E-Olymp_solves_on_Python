n = int(input())
a = list(map(float, input().split()))
d = 0
r = 0
for i in range(n):
    d = a[i]*10
    if d/int(d)==1:
        r = r+a[i]
print(r)
