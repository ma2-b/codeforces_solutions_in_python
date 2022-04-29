n = input()
count =0
for i in n:
    if i=="7" or i=="4":
        count+=1
a_countr=0
for j in str(count):
    if j=="4" or j=="7":
        a_countr+=1
if a_countr==len(str(count)):
    output="YES"
else:
    output="NO"
print(output)