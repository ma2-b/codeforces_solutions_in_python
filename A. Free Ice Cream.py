n,x = list(map(int,input().split()))
distressed = 0
remain = x
for i in range(n):
    a = input().split()
    if a[0] == "+":
        remain+=int(a[1])
    else:
        remain-=int(a[1])
        if remain < 0:
            remain+=int(a[1])    
            distressed+=1
print(remain,distressed)