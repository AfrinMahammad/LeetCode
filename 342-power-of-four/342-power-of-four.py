class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        elif n==1:
            return True
        else:
            while n>0:
                n=n/4
                if n==1:
                    return True
            return False