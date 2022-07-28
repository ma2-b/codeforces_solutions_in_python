a1,a2 = list(map(int,input().split()))
cnt = 0 
while a1 > 0 and a2> 0:
    if a1 == 1 and a2 == 1:
        break 
    if a1 > a2:
        a1-=2 
        a2+=1 
    else:
        a1+=1 
        a2-=2 
    cnt+=1 
print(cnt)