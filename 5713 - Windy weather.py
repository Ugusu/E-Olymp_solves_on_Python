n = int(input())
g = list(map(int, input().split()))
min = g[0]
max = g[0]
for i in range(n):
    if g[i]<min:
        min = g[i]
for i in range(n):
    if g[i]>max:
        max = g[i]
print(int(max-min))
