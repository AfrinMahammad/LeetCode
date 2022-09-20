class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=s.split(" ")
        print(l)
        while "" in l:
            l.remove("")
        print(l)
        return len(l[-1])