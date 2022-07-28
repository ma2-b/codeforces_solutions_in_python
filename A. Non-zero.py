a = int(input())
c = 0
d = 0
k = 0
for i in range(a):
	h = int(input())
	b = input().split()
	while True:
		k = k + int(b[d])
		d+=1
		if h == d:
			break
	for o in b:
		if o in "0":
			c+=1
	if c+k==0:
		print(c+1)
	else :
		print(c)
	d*=0
	c*=0
	k*=0