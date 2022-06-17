t = int(input())
for _ in range(t):
    a,b,c = list(map(int,input().split()))
    new_a = b - (c - b)
    new_b = a + (c - a) / 2
    new_c = a + 2*(b - a) 
    if new_a >= a and new_a % a == 0 and new_a != 0:
        print("YES")
    elif new_b >= b and (c-a)%2 == 0 and new_b % b == 0 and new_b != 0 :
        print("YES")
    elif new_c >= c and new_c % c == 0 and new_c != 0 :
        print("YES")
    else:   
        print("NO")