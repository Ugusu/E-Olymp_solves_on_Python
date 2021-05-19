a, b = map(int, input().split())
th = h = t = p = 0
i = a
while i <= b:
    th = i//1000
    h = (i - th*1000)//100
    t = (i - th*1000 - h*100)//10
    p = i -th*1000 - h*100 - t*10
    if th!=h and th!=t and th!=p and h!=t and h!=p and t!=p:
        print(i, end=' ')
    i = i+1
print()
