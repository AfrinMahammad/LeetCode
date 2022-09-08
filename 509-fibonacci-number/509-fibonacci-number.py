class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            t1,t2=0,1
            res=0
            for i in range(1,n):
                res=t1+t2
                t1=t2
                t2=res
            return res