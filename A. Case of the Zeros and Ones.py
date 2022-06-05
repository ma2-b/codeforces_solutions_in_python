n = int(input())
zo = input()
l = []
o = 0
z = 0
count = 0 
for i in zo:
    l.append(i)
for j in range(n):
    if l[j]=="1":
        o+=1
    else:
        z+=1
z = min(z,o)
print(n-(2*z))