t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    sort = True    
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            sort = False
    zero = False
    one = False 
    for i in range(len(brr)):
        if brr[i] == 0:
            zero = True 
        elif brr[i] == 1:
            one = True
    if sort == True :
        print("YES")
    else:
        if one == False or zero == False:
            print("NO")
        else:
            print("YES")