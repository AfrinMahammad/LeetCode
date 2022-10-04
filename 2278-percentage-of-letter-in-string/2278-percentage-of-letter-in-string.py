class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        import math
        if letter not in s:
            return 0
        c=0
        for i in s:
            if i==letter:
                c+=1
        return math.floor((c/len(s))*100)