class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r,c=[],[]
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                 if matrix[i][j]==0:
                    if i not in r:
                        r.append(i)
                    if j not in c:    
                        c.append(j)
        for i in r:
            for j in range(len(matrix[i])):
                matrix[i][j]=0
        for i in c:
            for j in range(len(matrix)):
                matrix[j][i]=0  
        