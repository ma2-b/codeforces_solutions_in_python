k,n,w = list(map(int,input().split()))
count=0
for i in range(1,w+1):
    count=count+i*k
result = count-n
if result < 0:
    result=0
print(result)   