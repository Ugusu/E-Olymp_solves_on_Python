n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i]>=0:
        a[i] = a[i]+2
for i in a:
    print(i, end=' ')
print()
