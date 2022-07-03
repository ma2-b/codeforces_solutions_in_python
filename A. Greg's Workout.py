n = int(input())
a = list(map(int,input().split()))
chest,biceps,back = 0,0,0
counter = 0
for i in a:
    if counter > 2:
        counter = 0
    if counter == 0:
        chest+=i 
        counter+=1
    elif counter == 1:
        biceps+=i
        counter+=1
    elif counter == 2:
        back+=i
        counter+=1
if chest > biceps and chest> back:
    print("chest")
elif biceps > chest and biceps > back:
    print("biceps")
else:
    print("back")