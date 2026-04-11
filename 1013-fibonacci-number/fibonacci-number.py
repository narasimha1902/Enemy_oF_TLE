class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        a,b=0,1
        for i in range(2,n):
            a,b=b,a+b
        return a+b
