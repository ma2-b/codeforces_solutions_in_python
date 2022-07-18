n = int(input())
counter = 0
min = 101
for _ in range(n):
    a,p = list(map(int,input().split()))
    if p <= min:
        counter+=(a*p)
        min = p    
    else:
        counter+=(min*a)
print(counter)