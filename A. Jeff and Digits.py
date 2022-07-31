n = int(input())
a = list(map(int,input().split()))
f,z = 0,0
for i in a:
    if i == 0:
        z+=1 
    elif i == 5:
        f+=1 
if z == 0:
    print(-1)
elif f < 9:
    print(0)
else:
    f -= f % 9
    for j in range(f):
        print(5,end="")
    for y in range(z):
        print(0,end="")
    print()