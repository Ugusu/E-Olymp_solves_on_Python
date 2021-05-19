n = int(input())
a = list(map(int, input().split()))
zcounter = 0
for i in range(n):
    if a[i] == 0:
        zcounter+=1

for i in range(zcounter):
    a.remove(0)
    a.append(0)

print(*a)
