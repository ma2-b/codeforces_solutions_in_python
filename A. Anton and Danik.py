n = int(input())
s = input()
d=0
a=0
for i in s:
    if i == "D":
        d+=1
    else:
        a+=1
if a>d:
    print("Anton")
elif a==d:
    print("Friendship")
else:
    print("Danik")