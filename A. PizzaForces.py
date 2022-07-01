class Solution:
    def pizza(self, n: int):
        if n < 6:
            return 15
        start = 15
        if n%2==0:
            n-=1  
        n = n - 4
        if n%2==0:
            floor = n/2
        else:
            floor = n//2 
        start += floor * 5
        return start
t = int(input())
for _ in range(t):
    n = int(input())
    obj = Solution()
    print(obj.pizza(n))