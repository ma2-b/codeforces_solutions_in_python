n,c = list(map(int,input().split()))
a = list(map(int,input().split()))
words = 0 
for i in range(n-1):
    if a[i+1] - a[i] > c:
        words = 0 
    else:
        words+=1 
print(words+1)