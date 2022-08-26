from itertools import permutations
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if n==1:
            return True
        l=[]
        for i in str(n):
            l.append(i)
        p=permutations(l,len(l))
        for i in list(p):
            if i[0]=='0':
                continue
            elif i[-1] in ['2','4','6','8']:
                x="".join(list(i))
                s=str(format(int(x),'b'))
                flag=1
                for i in s[1:]:
                    if i=='1':
                        flag=0
                        continue
                if flag==1:
                    return True
        return False   