import sys
from functools import reduce
from collections import Counter 
def ip(): return int(sys.stdin.readline())
def fip(): return float(sys.stdin.readline())
def sip() : return input()
def mip(): return map(int,sys.stdin.readline().split())
def mips(): return map(str,sys.stdin.readline().split())
def lip(): return list(map(int,sys.stdin.readline().split()))
def slip(): return list(map(str,sys.stdin.readline().split()))
def matip(n,m):
    lst=[]
    for i in range(n):
        arr = lip()
        lst.insert(i,arr)
    return lst
def factors(n): # find the factors of a number
    return list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def minJumps(arr, n): #to reach from 0 to n-1 in the array in minimum steps
    jumps = [0 for i in range(n)]
    if (n == 0) or (arr[0] == 0):
        return float('inf')
    jumps[0] = 0
    for i in range(1, n):
        jumps[i] = float('inf')
        for j in range(i):
            if (i <= j + arr[j]) and (jumps[j] != float('inf')):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    return jumps[n-1]
def dic(arr): # converting list into dict of count
    return Counter(arr)
def check_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**(0.5))+1,2):
        if n%i==0:
            return False
    return True 
n = ip()
while(n):
    n-=1
    s = sip()
    a = 0
    b = 0
    c = 0
    for item in s:
        if item=="A":
            a+=1
        elif item=="B":
            b+=1
        else:
            c+=1
    if a+c==b:
        print("YES")
    else:
        print("NO")