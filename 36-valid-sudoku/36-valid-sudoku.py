class Solution:
    def isValidSudoku(self, b: List[List[str]]) -> bool:
        temp=[]
        for i in range(0,9):
            temp=[]
            for j in range(0,9):
                if b[i][j]==".":
                    continue
                elif b[i][j] in temp:
                    return False
                else:
                    temp.append(b[i][j])
        for i in range(0,9):
            temp=[]
            for j in range(0,9):
                if b[j][i]==".":
                    continue
                elif b[j][i] in temp:
                    return False
                else:
                    temp.append(b[j][i])
        i=0
        while i<9:
            j=0
            while j<9:
                m=0
                temp=[]
                while m<3:
                    n=0
                    while n<3:
                        if b[i+m][j+n]!=".":
                            if b[i+m][j+n] in temp:
                                return False
                            else:
                                temp.append(b[i+m][j+n])
                        n+=1
                    m+=1
                j+=3
            i+=3
        return True       
            