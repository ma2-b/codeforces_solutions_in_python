t = int(input())
mishka = 0
chirs = 0
for _ in range(t):
    n,m = list(map(int,input().split()))
    if n > m:
        mishka+=1 
    elif n < m:
        chirs+=1
if mishka > chirs:
    print("Mishka")
elif chirs > mishka:
    print("Chris")
else:
    print("Friendship is magic!^^")
