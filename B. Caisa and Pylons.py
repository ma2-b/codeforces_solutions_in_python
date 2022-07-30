n = int(input())
h = list(map(int,input().split()))
x = 0 
energy,sol = 0,0
for y in h:
    energy+=(x-y)
    if energy < 0:
        sol+=(-energy)
        energy = 0 
    x = y 
print(sol)