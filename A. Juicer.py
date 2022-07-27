n,b,d = list(map(int,input().split()))
a = list(map(int,input().split()))
result = 0 
dtimes = 0
for i in a:
    if i <= b:
        result+=i 
    if result > d:
        dtimes+=1 
        result = 0
print(dtimes)