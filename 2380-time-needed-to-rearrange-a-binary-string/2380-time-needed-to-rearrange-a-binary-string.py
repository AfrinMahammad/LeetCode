class Solution(object):
    def secondsToRemoveOccurrences(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        while '01' in s:
            s=s.replace('01','10')
            res+=1
        return res