class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        n=len(words)
        if n==1 or n==0:
            return n
        a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res=[]
        for i in words:
            x=""
            for j in i:
                x=x+code[a.index(j)]
            if x not in res:
                res.append(x)
        return len(res)