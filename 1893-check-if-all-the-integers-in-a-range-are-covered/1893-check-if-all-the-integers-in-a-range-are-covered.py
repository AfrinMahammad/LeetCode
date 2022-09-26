class Solution:
    def isCovered(self, a: List[List[int]],l:int,r:int)-> bool:
        a.sort()
        for i in a:
            if i[0]>r or i[1]<l:
                continue
            elif i[0]<=l and i[1]>=r:
                return True
            elif i[0]<=l:
                l=i[1]+1
                if l>r:
                    return True
            elif i[1]>=r:
                r=i[0]-1
                if l>r:
                    return True
        return False