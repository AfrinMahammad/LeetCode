class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        elif n==1:
            return True
        else:
            return True if sorted(format(n,'b'),reverse=True)[1]=='0' else False