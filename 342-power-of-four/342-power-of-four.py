class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        elif n==1:
            return True
        else:
            t=1
            while t<n:
                t=t*4
                if t==n:
                    return True
            return False