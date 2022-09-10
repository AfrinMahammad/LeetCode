class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l1,l2=[],[]
        for i in s:
            if i=='#':
                if len(l1)>0:
                    l1.pop()
            else:
                l1.append(i)
        for i in t:
            if i=='#':
                if len(l2)>0:
                    l2.pop()
            else:
                l2.append(i)
        if l1==l2:
            return True
        return False