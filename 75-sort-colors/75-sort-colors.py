class Solution:
    def sortColors(self, s: List[int]) -> None:
        n=len(s)
        for i in range(n):
            for j in range(n-i-1):
                if s[j]>s[j+1]:
                    temp=s[j]
                    s[j]=s[j+1]
                    s[j+1]=temp
        return s