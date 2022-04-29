n = list(input())
r_n = input()
r = list(reversed(n))
result=""
for i in r:
    result+=i
if result==r_n:
    print("YES")
else:
    print("NO")