y = int(input())
while True:
    y+=1 
    a=y//1000
    b=(y%1000)//100
    c=((y%1000)%100)//10
    d=((y%1000)%100)%10
    if a != b and a != c and a != d and b != c and b != d and c != d:
        break 
print(y)
