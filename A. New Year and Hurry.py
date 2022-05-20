n,k = list(map(int,input().split()))
limt = 240
time_to_solve = limt-k
counter=0
for i in range(n+1):
    if time_to_solve-(5*i) >= 0:
        counter+=1
        time_to_solve-=(5*i) 
print(counter-1)