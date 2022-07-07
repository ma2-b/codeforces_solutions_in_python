n = int(input())
b = list(map(int,input().split()))
m = 0
for index,i in enumerate(b):
    if index == 0:
        print(i,end=" ")
        m = i 
    else:
        print(i+m,end=" ")
        m = max(m,(i+m))
    
    