d1,d2,d3 = list(map(int,input().split()))
a1=d1+d2+d3
a2=2*d1+2*d2
a3=2*d1+2*d3
a4=2*d2+2*d3
result = min(a1,min(a2,min(a3,a4)))
print(result)