n,m = list(map(int,input().split()))
counter = 0 
a = 0 
while a * a <= n and a <= m:
    b = n - a * a
    if a + b * b == m:
        counter+=1
    a+=1
print(counter)