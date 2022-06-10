from math import floor
n,s = list(map(int,input().split()))
total = floor((s+n-1)/n) 
print(total)