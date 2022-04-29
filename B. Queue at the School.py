a = list(map(int,input().split()))
c= input()
b = list(c)
d = ""
while (a[1]>0):
	i=0
	while i<(len(b)-1):
		if (b[i]=='B' and b[i+1]=='G'):
			b[i],b[i+1]=b[i+1],b[i]
			i+=1
		i+=1
	a[1]-=1
for i in range(len(b)):
	d+=b[i]
print(d)