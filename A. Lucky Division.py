# Its doing runtime error
n = int(input())
flag = False 
arr = [4,7,47,74,44,444,447,474,477,777,774,744]
for i in range(12):
    if n % arr[i] == 0:
        flage = True 
if flage:
    print('YES')
else:
    print('NO')