class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        acc=0
        for i in range(k):
            if blocks[i]=="W":
                acc+=1
        ret=acc
        for i in range(k,len(blocks)):
            if blocks[i]=="W":
                acc+=1
            if blocks[i-k]=="W":
                acc-=1
            ret=min(ret,acc)
        return ret