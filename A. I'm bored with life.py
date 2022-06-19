n,m = list(map(int,input().split()))
a = 1
b = 1 
for i in range(2,(min(n,m))+1):
    a *= i 
print(a)