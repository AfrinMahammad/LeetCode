class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b=format(n,'b')
        if '11' in b or '00' in b:
            return False
        return True