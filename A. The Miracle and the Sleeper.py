t = int(input())
for _ in range(t):
    l,r = list(map(int,input().split()))
    half = r//2 
    if l > half:
        print(r%l) 
    else:
        print( r % (half + 1))