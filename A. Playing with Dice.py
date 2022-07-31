a,b = list(map(int,input().split()))
f,s,d = 0,0,0
for i in range(1,7):
    if abs(a - i) < abs(b - i):
        f+=1 
    elif abs(b - i) < abs(a - i):
        s+=1 
    else:
        d+=1
print(f,d,s)