class Solution:    
    def find(self,l):
        x=l[0]
        l.sort()
        for i in range(len(l)):
            if l[i]>x:
                l[0],l[i]=l[i],l[0]
                y=l[0:1]
                z=sorted(l[1:])
                y.extend(z)  
                return y              
    def nextPermutation(self,p)->None:
        n=len(p)
        y=[]
        if p==sorted(p,reverse=True):
            p.sort()
        elif p[n-1]>p[n-2]:
            p[n-2],p[n-1]=p[n-1],p[n-2]
        else:
            for i in range(n-2,0,-1):
                if p[i]>p[i-1]:
                    t=Solution().find(p[i-1:])
                    print(t)
                    x=i-1
                    for k in t:
                        p[x]=k
                        x+=1
                    break
                        