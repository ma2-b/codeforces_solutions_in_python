s = input()
lower = []
upper = []
for i in s:
   if i.islower():
       lower.append(i)
   else:
       upper.append(i)
if len(upper)>len(lower):
   print(s.upper())
else:
   print(s.lower())