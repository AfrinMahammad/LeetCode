class Solution:
    def intToRoman(self, num: int) -> str:
        res=""
        mapping={'1':'I','5':'V','10':'X','50':'L','100':'C','500':'D','1000':'M'}
        s=str(num)
        i=1
        while i<=len(s):
            if s[-i]=='1':
                if i==1:
                    res='I'+res
                elif i==2:
                    res='X'+res
                elif i==3:
                    res='C'+res
                else:
                    res='M'+res
            elif s[-i]=='2':
                if i==1:
                    res=2*'I'+res
                elif i==2:
                    res=2*'X'+res
                elif i==3:
                    res=2*'C'+res
                else:
                    res=2*'M'+res
            elif s[-i]=='3':
                if i==1:
                    res=3*'I'+res
                elif i==2:
                    res=3*'X'+res
                elif i==3:
                    res=3*'C'+res
                else:
                    res=3*'M'+res
            elif s[-i]=='4':
                if i==1:
                    res='IV'+res
                elif i==2:
                    res='XL'+res
                else:
                    res='CD'+res
            elif s[-i]=='5':
                if i==1:
                    res='V'+res
                elif i==2:
                    res='L'+res
                else:
                    res='D'+res
            elif s[-i]=='6':
                if i==1:
                    res='VI'+res
                elif i==2:
                    res='LX'+res
                else:
                    res='DC'+res
            elif s[-i]=='7':
                if i==1:
                    res='VII'+res
                elif i==2:
                    res='LXX'+res
                else:
                    res='DCC'+res
            elif s[-i]=='8':
                if i==1:
                    res='VIII'+res
                elif i==2:
                    res='LXXX'+res
                else:
                    res='DCCC'+res
            elif s[-i]=='9':
                if i==1:
                    res='IX'+res
                elif i==2:
                    res='XC'+res
                else:
                    res='CM'+res
            i+=1
        return res 