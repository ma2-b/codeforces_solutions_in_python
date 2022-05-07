from math import sqrt
x,y,z = list(map(int,input().split()))
a = sqrt((x*y)//z)
b = sqrt((x*z)//y)
c = sqrt((y*z)//x)
val = (a+b+c)*4
print(int(val))