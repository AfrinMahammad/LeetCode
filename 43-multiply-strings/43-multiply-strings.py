class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        i,j=0,0
        res=0
        if num1=='0' or num2=='0':
            return '0'
        elif num1=='1':
            return num2
        elif num2=='1':
            return num1
        else:
            n=int(num1)
            i,p=len(num2)-1,1
            while i>=0:
                t=int(num2[i])*n
                res=res+p*t
                p=p*10
                i-=1
            return str(res)