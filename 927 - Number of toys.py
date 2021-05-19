n = int(input())
r = 0
for i in range(n):
    a, b = map(float, input().split())
    if b < 50:
        r = r+a
print(int(r))
