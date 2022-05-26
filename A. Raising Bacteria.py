x = int ( input ( ) )
sol = 0
while x > 0:
    if x % 2 == 1:
        sol += 1 
    x //= 2 
print(sol) 