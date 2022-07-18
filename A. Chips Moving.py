n = int(input())
x = list(map(int,input().split()))
counter = 0 
for i in x:
    counter+= i & 1 
print(min(counter,n - counter))