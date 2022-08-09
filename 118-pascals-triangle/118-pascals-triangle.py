class Solution(object):
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l=[]
        for i in range(n):
            x=[]
            for j in range(i+1):
                x.append(0)
            l.append(x)  
        for i in range(0,n):
            l[i][0]=1
            l[i][i]=1
        if n>2:    
            for i in range(2,n):
                for j in range(1,i):
                    l[i][j]=l[i-1][j-1]+l[i-1][j]
        return l