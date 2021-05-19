n = int(input())
a = list(map(int, input().split()))
r = []
for i in a:
    if i%2!=0:
        r.append(i)
for i in r:
    print(i, end=' ')
print()
