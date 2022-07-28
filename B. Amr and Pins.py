from math import ceil, sqrt
r,x,y,X,Y = list(map(int,input().split()))
dst=sqrt((X-x)*(X-x)+(Y-y)*(Y-y))
print(ceil(dst/(2*r)))