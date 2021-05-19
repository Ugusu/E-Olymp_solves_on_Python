n = int(input())
a = list(map(int, input().split()))
max1 = max2 = -101
for i in range(n):
    if a[i] > max1:
        a.append(max1)
        max1 = a[i]

a.remove(max1)

for i in range(n-1):
    if a[i] > max2:
        a.append(max2)
        max2 = a[i]
print(max1+max2)
