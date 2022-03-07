class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        base=ord("A")
        ret=[]
        for i in range(ord(s[0])-base,ord(s[3])-base+1):
            for j in range(int(s[1]),int(s[4])+1):
                ret.append(chr(base+i)+str(j))
        return ret