a, b = map(int, input().split())

while a <= b:
    t = str(a)
    l = False
    for i in t:
        if int(i)%2==0:
            l = True
            break
    if not l:
        print(t, end = ' ')

    a = a+1
    
print()
