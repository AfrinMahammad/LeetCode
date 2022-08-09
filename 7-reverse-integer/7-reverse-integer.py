class Solution:
    def reverse(self, x: int) -> int:
        p=pow(2,31)
        if x<0:
            s=str(x)[1:]
        else:
            s=str(x)
        while s.endswith('0')=='0':
            s=s[:len(s)-1]
        t=s[::-1]
        if int(t)>(p-1) or int(t)<-p:
            return 0
        else:
            if x<0:
                return -int(t)
            else:
                return int(t)
         