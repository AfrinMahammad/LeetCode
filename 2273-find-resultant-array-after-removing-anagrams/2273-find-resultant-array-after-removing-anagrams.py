class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i=1
        while i<len(words):
            if sorted(words[i-1])==sorted(words[i]):
                del words[i]
                i-=1
            i+=1
        return words