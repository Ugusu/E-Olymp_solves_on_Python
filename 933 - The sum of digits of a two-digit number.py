n = int(input())
sum = 0
for i in str(n):
    if i != '-':
        sum = sum + int(i)
print(sum)
