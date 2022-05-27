a,b = list(map(int,input().split()))
hours = a
while(a >= b):
    d = a // b
    hours += d
    m = a % b
    a = d + m
print(hours)