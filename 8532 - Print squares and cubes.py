a, b = map(int, input().split())
i = a

while i <= b:
    print(i**2, end=' ')
    i = i+1

print()
i = b

while i >= a:
    print(i**3, end=' ')
    i = i-1

print()
