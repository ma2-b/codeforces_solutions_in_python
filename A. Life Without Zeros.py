a = int(input())
b = int(input())
c = a + b 
a_0 = ""
b_0 = ""
c_0 = ""
for i in str(a):
    if str(i) != "0":
        a_0+=i 
for i in str(b):
    if str(i) != "0":
        b_0+=i 
for i in str(c):
    if str(i) != "0":
        c_0+=i 
if int(a_0) + int(b_0) == int(c_0):
    print("YES")
else:
    print("NO")