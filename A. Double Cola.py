n = int(input())
n-=1
a = ['Sheldon','Leonard','Penny','Rajesh','Howard']
i = 5
while n>=i:
    n-=i
    i*= 2
print(a[n//(i//5)])